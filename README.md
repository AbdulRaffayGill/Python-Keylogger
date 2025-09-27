![Logo](plut.ico)



# Plutonium
A Python Keylogger that when triggered , record every keystrokes of the victim , until Esc is pressed.
Once Esc is pressed, it stops , create a new text file based on the name of current user, stores the recorded keystrokes in it and upload it to airforshare.com
This can be used in same network attacks where sensitive information from victim needs to be extracted 
This Keylogger works as a background process completely, so basic stealth mechanism is implemented.
To compile the code , You need to install **pyinstaller** module.
Once installed , use this command

`pyinstaller --onefile --windowed --name='Plutonium' --icon='plut.ico' key.py`

 # Internal Working

Persistence Mechanism:

Copies itself to the Windows Temp directory (%TEMP%)
Registers a startup entry in the Windows Registry (HKCU\Software\Microsoft\Windows\CurrentVersion\Run) to execute automatically on user login
Uses the current Python executable path for replication

Utilizes the keyboard library to capture all keystrokes in real-time
Saves captured keystrokes to a text file in the user's Music folder
Names the log file after the computer's hostname (e.g., john.txt)
Data Exfiltration:

Automatically uploads the keystroke log file to airforshare.com
Uses HTTP POST request with multipart file upload
Includes authentication parameters in the upload request
Execution Flow:

Script copies itself to the Temp directory for persistence
Registers itself to run at Windows startup
Begins recording all keystrokes immediately
Stops recording when user presses ESC key
Writes all captured keystrokes to a timestamped log file
Automatically uploads the log file to a remote file-sharing service

