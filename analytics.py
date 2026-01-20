import requests
import json
import uuid
import os
import threading
import platform

class AnalyticsTracker:
    MEASUREMENT_ID = "G-7T34QEG0SS"
    API_SECRET = "rkHgSgByTLWdyQElF-bbIw"
    BASE_URL = f"https://www.google-analytics.com/mp/collect?measurement_id={MEASUREMENT_ID}&api_secret={API_SECRET}"

    def __init__(self):
        self.client_id = self._get_or_create_client_id()
        # Session ID is unique for each run of the app
        self.session_id = str(uuid.uuid4())

    def _get_or_create_client_id(self):
        # Store in user's home directory to persist across runs/updates
        # This ensures we count unique users correctly even if they move the exe
        config_dir = os.path.join(os.path.expanduser("~"), ".kruti_dev_converter")
        config_file = os.path.join(config_dir, "client_id.txt")
        
        if os.path.exists(config_file):
            try:
                with open(config_file, "r") as f:
                    cid = f.read().strip()
                    if cid:
                        return cid
            except:
                pass
        
        # Create new
        client_id = str(uuid.uuid4())
        try:
            os.makedirs(config_dir, exist_ok=True)
            with open(config_file, "w") as f:
                f.write(client_id)
        except:
            pass # Fail silently if can't write, will just generate new ID next time
            
        return client_id

    def _send_event(self, event_name, params=None):
        def _send():
            if params is None:
                payload_params = {}
            else:
                payload_params = params.copy()
            
            payload_params["session_id"] = self.session_id
            # Add basic user agent info if possible, though GA4 relies on client_id mostly for user counts
            
            payload = {
                "client_id": self.client_id,
                "events": [{
                    "name": event_name,
                    "params": payload_params
                }]
            }
            
            try:
                # Use a short timeout so we don't hang if internet is bad
                requests.post(self.BASE_URL, json=payload, timeout=5)
            except:
                pass # Fail silently, analytics shouldn't crash the app

        # Run in a separate thread to avoid blocking UI
        threading.Thread(target=_send, daemon=True).start()

    def track_app_launch(self):
        self._send_event("app_launch", {
            "os": platform.system(),
            "os_release": platform.release(),
            "python_version": platform.python_version()
        })

    def track_conversion(self, file_type, item_count, success=True):
        self._send_event("file_conversion", {
            "file_type": file_type,
            "items_converted": item_count,
            "success": str(success).lower()
        })
        
    def track_feature_use(self, feature_name):
        self._send_event("feature_use", {
            "feature_name": feature_name
        })
