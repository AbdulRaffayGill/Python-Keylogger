import os
import winreg

def register_hkcu(app_name: str, script_path: str):
    """
    Register a program to run at startup under HKCU\Software\Microsoft\Windows\CurrentVersion\Run
    - app_name: Name to show in registry
    - script_path: Absolute path of the script to run
    """
    run_key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    # Open HKCU with write access
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, run_key_path, 0, winreg.KEY_SET_VALUE | winreg.KEY_QUERY_VALUE) as run_key:
        try:
            # Check if already exists
            existing, _ = winreg.QueryValueEx(run_key, app_name)
            if existing == script_path:
                print(f"[i] Already registered: {app_name} → {script_path}")
                return
        except FileNotFoundError:
            pass  # No existing value

        # Register new value
        winreg.SetValueEx(run_key, app_name, 0, winreg.REG_SZ, script_path)
        print(f"[+] Registered: {app_name} → {script_path}")


if __name__ == "__main__":
    # Register the main script (key.py in your case)
    register_hkcu("testREG", os.path.abspath(__file__))
