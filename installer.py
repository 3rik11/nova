import os
import urllib.request
from pathlib import Path
import getpass
import win32com.client  # Requires: pip install pywin32

# ---- CONFIG ----
GITHUB_RAW_URL = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"
FOLDER_NAME = "NovaApp"
SCRIPT_NAME = "app.py"
SHORTCUT_NAME = "Launch Nova.lnk"
# ----------------

# Get user's desktop and target paths
username = getpass.getuser()
desktop_path = Path(f"C:/Users/{username}/Desktop")
documents_path = Path(f"C:/Users/{username}/Documents")
target_folder = documents_path / FOLDER_NAME
script_path = target_folder / SCRIPT_NAME
shortcut_path = desktop_path / SHORTCUT_NAME

# Make target folder
os.makedirs(target_folder, exist_ok=True)

# Download the file
print("Downloading app.py...")
urllib.request.urlretrieve(GITHUB_RAW_URL, script_path)
print("Download complete.")

# Create Windows Shortcut
print("Creating shortcut...")
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(str(shortcut_path))

# Set the target to run python in CMD with the app
shortcut.Targetpath = "cmd.exe"
shortcut.Arguments = f'/k python "{script_path}"'
shortcut.WorkingDirectory = str(target_folder)

# Use default .exe icon (shell32.dll index 2)
shortcut.IconLocation = "C:\\Windows\\System32\\shell32.dll,2"

# Save the shortcut
shortcut.save()
print("Shortcut created on desktop.")
