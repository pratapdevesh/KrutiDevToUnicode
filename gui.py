import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from file_handlers import FileHandler
from converter import KrutiDevConverter
import threading
import os
import sys
from PIL import Image
from analytics import AnalyticsTracker

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class ConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Kruti Dev Unicode Converter By Bhanu Pratap")
        self.geometry("800x700")
        
        self.file_handler = FileHandler()
        self.converter = KrutiDevConverter()
        self.selected_files = []
        
        # Initialize Analytics
        self.tracker = AnalyticsTracker()
        self.tracker.track_app_launch()
        
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1) # Main content
        self.grid_rowconfigure(1, weight=0) # Action buttons (Instructions/Donate)
        self.grid_rowconfigure(2, weight=0) # Footer

        # --- Main Content Frame ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=(20, 10))
        
        self.header_label = ctk.CTkLabel(self.main_frame, text="Kruti Dev <-> Unicode Converter", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=15)
        
        self.tabview = ctk.CTkTabview(self.main_frame)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.tabview.add("File Converter")
        self.tabview.add("Live Preview")
        
        self.setup_converter_tab(self.tabview.tab("File Converter"))
        self.setup_preview_tab(self.tabview.tab("Live Preview"))

        # --- Extra Actions Frame ---
        self.extra_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.extra_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=5)
        
        # Instructions Button
        btn_instr = ctk.CTkButton(self.extra_frame, text="Important Instructions / महत्वपूर्ण निर्देश", command=self.show_instructions, fg_color="gray", hover_color="gray30")
        btn_instr.pack(side="left", padx=10, expand=True, fill="x")

        # Donate Button
        btn_donate = ctk.CTkButton(self.extra_frame, text="Donate (Buy me a coffee) / सहयोग करें", command=self.show_donate, fg_color="#FFD700", text_color="black", hover_color="#E6C200")
        btn_donate.pack(side="right", padx=10, expand=True, fill="x")

        # --- Footer Frame ---
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
        
        dev_info = "Developer: Bhanu Pratap  |  Email: bhanunoteii@gmail.com  |  Mobile: +91-9755341179"
        self.lbl_footer = ctk.CTkLabel(self.footer_frame, text=dev_info, font=ctk.CTkFont(size=12, slant="italic"), text_color="gray70")
        self.lbl_footer.pack()

    def setup_converter_tab(self, parent):
        # Conversion Type
        self.conversion_var = ctk.StringVar(value="kd_to_unicode")
        
        frame_type = ctk.CTkFrame(parent)
        frame_type.pack(fill="x", padx=10, pady=10)
        
        lbl_type = ctk.CTkLabel(frame_type, text="Conversion Type:", font=ctk.CTkFont(weight="bold"))
        lbl_type.pack(side="left", padx=10)
        
        rb1 = ctk.CTkRadioButton(frame_type, text="Kruti Dev -> Unicode", variable=self.conversion_var, value="kd_to_unicode")
        rb1.pack(side="left", padx=10)
        
        rb2 = ctk.CTkRadioButton(frame_type, text="Unicode -> Kruti Dev", variable=self.conversion_var, value="unicode_to_kd")
        rb2.pack(side="left", padx=10)

        # File Selection
        frame_files = ctk.CTkFrame(parent)
        frame_files.pack(fill="both", expand=True, padx=10, pady=10)
        
        btn_select = ctk.CTkButton(frame_files, text="Browse Files", command=self.browse_files)
        btn_select.pack(pady=10)
        
        self.listbox_files = ctk.CTkTextbox(frame_files, height=150)
        self.listbox_files.pack(fill="both", expand=True, padx=10, pady=5)
        self.listbox_files.configure(state="disabled")

        # Action Buttons
        frame_actions = ctk.CTkFrame(parent, fg_color="transparent")
        frame_actions.pack(pady=10)
        
        self.btn_convert = ctk.CTkButton(frame_actions, text="Convert Now", command=self.start_conversion, font=ctk.CTkFont(size=15, weight="bold"), height=40, fg_color="#2CC985", hover_color="#229965")
        self.btn_convert.pack(side="left", padx=10)
        
        btn_clear = ctk.CTkButton(frame_actions, text="Clear List", command=self.clear_list, fg_color="#FF5555", hover_color="#CC4444")
        btn_clear.pack(side="left", padx=10)

        # Status & Progress
        self.progress = ctk.CTkProgressBar(parent)
        self.progress.pack(fill="x", padx=20, pady=(10, 5))
        self.progress.set(0)
        
        self.lbl_status = ctk.CTkLabel(parent, text="Ready", text_color="gray80")
        self.lbl_status.pack(pady=5)

    def setup_preview_tab(self, parent):
        lbl_instr = ctk.CTkLabel(parent, text="Paste text below to test conversion logic:")
        lbl_instr.pack(pady=5, anchor="w", padx=10)
        
        self.txt_input = ctk.CTkTextbox(parent, height=100)
        self.txt_input.pack(fill="x", padx=10, pady=5)
        
        btn_update = ctk.CTkButton(parent, text="Update Preview", command=self.update_preview, height=25)
        btn_update.pack(pady=5)
        
        self.preview_mode = ctk.StringVar(value="kd_to_unicode")
        frame_opts = ctk.CTkFrame(parent, fg_color="transparent")
        frame_opts.pack(pady=5)
        
        rb_p1 = ctk.CTkRadioButton(frame_opts, text="Kruti Dev -> Unicode", variable=self.preview_mode, value="kd_to_unicode", command=self.update_preview)
        rb_p1.pack(side="left", padx=10)
        rb_p2 = ctk.CTkRadioButton(frame_opts, text="Unicode -> Kruti Dev", variable=self.preview_mode, value="unicode_to_kd", command=self.update_preview)
        rb_p2.pack(side="left", padx=10)

        lbl_out = ctk.CTkLabel(parent, text="Converted Output:")
        lbl_out.pack(pady=5, anchor="w", padx=10)
        
        self.txt_output = ctk.CTkTextbox(parent, height=100, state="disabled", fg_color=("gray85", "gray20"))
        self.txt_output.pack(fill="x", padx=10, pady=5)

    def update_preview(self, event=None):
        text = self.txt_input.get("1.0", "end").strip()
        if not text:
            self.txt_output.configure(state="normal")
            self.txt_output.delete("1.0", "end")
            self.txt_output.configure(state="disabled")
            return
        
        mode = self.preview_mode.get()
        if mode == "kd_to_unicode":
            converted = self.converter.convert_to_unicode(text)
        else:
            converted = self.converter.convert_to_krutidev(text)
            
        self.tracker.track_feature_use("live_preview")
            
        self.txt_output.configure(state="normal")
        self.txt_output.delete("1.0", "end")
        self.txt_output.insert("1.0", converted)
        self.txt_output.configure(state="disabled")

    def show_instructions(self):
        msg_eng = ("After the conversion is complete, don't forget to change the text formatting in your "
                   "Excel/Word file by switching the fonts from KrutiDev to Arial/Cambria/etc.\n\n"
                   "Additionally, numbers containing a '/' (forward slash) may have converted into 'ध्'; "
                   "please ensure you replace those back with a '/'.")
        
        msg_hin = ("कन्वर्जन पूरा होने के बाद, अपनी Excel/Word फाइल में टेक्स्ट फॉर्मेटिंग को "
                   "KrutiDev से बदलकर Arial/Cambria/इत्यादि करना न भूलें।\n\n"
                   "साथ ही, जिन नंबरों में '/' (फॉरवर्ड स्लैश) का इस्तेमाल हुआ है, वे बदलकर 'ध्' हो गए होंगे; "
                   "कृपया उन्हें वापस '/' से बदल (replace) लें।")
        
        self.tracker.track_feature_use("instructions_viewed")
        
        win = ctk.CTkToplevel(self)
        win.title("Important Instructions")
        win.geometry("600x400")
        
        ctk.CTkLabel(win, text="Instructions / निर्देश", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        
        textbox = ctk.CTkTextbox(win, width=550, height=300)
        textbox.pack(pady=10)
        textbox.insert("1.0", "ENGLISH:\n" + msg_eng + "\n\n" + "-"*40 + "\n\nHINDI:\n" + msg_hin)
        textbox.configure(state="disabled")

    def show_donate(self):
        self.tracker.track_feature_use("donate_viewed")
        win = ctk.CTkToplevel(self)
        win.title("Support Development")
        win.geometry("500x650")
        
        txt_eng = ("Love this app? Support its development! This app is a solo project, and your tips keep me "
                   "motivated to add new features. Buy me a coffee to show your support!")
        txt_hin = ("ऐप पसंद आया? इसके विकास में सहयोग करें! यह ऐप मेरा एक सोलो प्रोजेक्ट है, और आपकी छोटी सी "
                   "मदद मुझे नए फीचर्स जोड़ने के लिए प्रेरित करती है। अपना समर्थन दिखाने के लिए आप मुझे एक "
                   "कॉफी 'Buy me a coffee' भेंट कर सकते हैं!")
        
        ctk.CTkLabel(win, text="Buy me a Coffee! \u2615", font=ctk.CTkFont(size=20, weight="bold"), text_color="#FFD700").pack(pady=10)
        
        lbl_msg = ctk.CTkLabel(win, text=txt_eng + "\n\n" + txt_hin, wraplength=450, font=ctk.CTkFont(size=13))
        lbl_msg.pack(pady=10, padx=20)

        # Allow layout to settle before handling image dimensions if needed, or just pack
        try:
            img_path = resource_path("donate_qr.jpg")
            pil_img = Image.open(img_path)
            # Resize image to fit nicely
            pil_img = pil_img.resize((300, 300), Image.Resampling.LANCZOS)
            qr_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(300, 300))
            
            lbl_img = ctk.CTkLabel(win, image=qr_img, text="")
            lbl_img.pack(pady=20)
        except Exception as e:
            ctk.CTkLabel(win, text=f"(QR Code Image Missing: {e})", text_color="red").pack(pady=20)

    def browse_files(self):
        filenames = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=(("All Supported", "*.txt *.xlsx *.docx"), ("Text Files", "*.txt"), ("Excel Files", "*.xlsx"), ("Word Files", "*.docx"))
        )
        for filename in filenames:
            if filename not in self.selected_files:
                self.selected_files.append(filename)      
        self.update_file_list()

    def update_file_list(self):
        self.listbox_files.configure(state="normal")
        self.listbox_files.delete("1.0", "end")
        for f in self.selected_files:
            self.listbox_files.insert("end", os.path.basename(f) + "\n")
        self.listbox_files.configure(state="disabled")

    def clear_list(self):
        self.selected_files = []
        self.update_file_list()
        self.lbl_status.configure(text="List cleared")

    def start_conversion(self):
        if not self.selected_files:
            messagebox.showwarning("No Files", "Please select files to convert first.")
            return
        
        self.btn_convert.configure(state="disabled")
        self.progress.set(0)
        
        threading.Thread(target=self.run_conversion_thread, daemon=True).start()

    def run_conversion_thread(self):
        conversion_type = self.conversion_var.get()
        success_count = 0
        total_changes = 0
        results = []
        total_files = len(self.selected_files)

        for i, filepath in enumerate(self.selected_files):
            self.lbl_status.configure(text=f"Processing: {os.path.basename(filepath)}...")
            self.update_idletasks()
            
            success, msg, changes = self.file_handler.process_file(filepath, conversion_type)
            
            if success:
                success_count += 1
                total_changes += changes
                results.append(f"{os.path.basename(filepath)}: Success ({changes} items modified)")
                self.tracker.track_conversion(os.path.splitext(filepath)[1], changes, success=True)
            else:
                results.append(f"{os.path.basename(filepath)}: Failed - {msg}")
                self.tracker.track_conversion(os.path.splitext(filepath)[1], 0, success=False)
            
            self.progress.set((i + 1) / total_files)
        
        self.lbl_status.configure(text=f"Completed. {success_count}/{total_files} successful.")
        self.after(0, lambda: self.show_completion_message(success_count, results, total_changes))

    def show_completion_message(self, success_count, results, total_changes):
        self.btn_convert.configure(state="normal")
        msg_title = "Conversion Completed"
        msg_body = f"Successfully processed {success_count} files.\nTotal text items modified: {total_changes}\n\nDetails:\n" + "\n".join(results)
        if total_changes == 0 and success_count > 0:
             msg_body += "\n\nWARNING: 0 items were modified. Please check text matches."
             messagebox.showwarning(msg_title, msg_body)
        else:
            # Show Instructions after conversion as requested/implied for good UX
            if messagebox.askyesno(msg_title, msg_body + "\n\nWould you like to view important formatting instructions?"):
                self.show_instructions()

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()
