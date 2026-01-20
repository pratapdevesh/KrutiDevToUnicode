import sys
import subprocess
import pkg_resources
import ctypes

def check_dependencies():
    required = {'openpyxl', 'python-docx', 'customtkinter', 'packaging', 'Pillow'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    
    if missing:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing], 
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            sys.exit(1)

def show_error(message):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, str(message), "Example Error", 0x10)

def main():
    if not getattr(sys, 'frozen', False):
        check_dependencies()
    
    try:
        import gui
        # ConverterApp is now a ctk.CTk class (window itself), so we don't pass a root to it.
        app = gui.ConverterApp()
        app.mainloop()
    except Exception as e:
        # If we are compiled as --noconsole, standard print/input won't work.
        # Use a native message box to show the crash error.
        import traceback
        error_msg = f"An error occurred:\n{str(e)}\n\n{traceback.format_exc()}"
        show_error(error_msg)

if __name__ == "__main__":
    main()
