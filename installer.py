import os
import urllib.request
from pathlib import Path
import getpass
import win32com.client  # Requires: pip install pywin32

# ---- CONFIG ----
GITHUB_RAW_APP_URL = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"
GITHUB_RAW_UPDATER_URL = "https://raw.githubusercontent.com/3rik11/nova/main/updater.py"
FOLDER_NAME = "NovaApp"
APP_SCRIPT_NAME = "app.py"
UPDATER_SCRIPT_NAME = "updater.py"
SHORTCUT_NAME = "Launch Nova.lnk"
# ----------------

# Get user's desktop and target paths
username = getpass.getuser()
desktop_path = Path(f"C:/Users/{username}/Desktop")
documents_path = Path(f"C:/Users/{username}/Documents")
target_folder = documents_path / FOLDER_NAME
app_script_path = target_folder / APP_SCRIPT_NAME
updater_script_path = target_folder / UPDATER_SCRIPT_NAME
shortcut_path = desktop_path / SHORTCUT_NAME

# Make target folder
os.makedirs(target_folder, exist_ok=True)

# Download the app.py file
print("Downloading app.py...")
urllib.request.urlretrieve(GITHUB_RAW_APP_URL, app_script_path)
print("app.py download complete.")

# Download the updater.py file
print("Downloading updater.py...")
urllib.request.urlretrieve(GITHUB_RAW_UPDATER_URL, updater_script_path)
print("updater.py download complete.")

# Create Windows Shortcut
print("Creating shortcut...")
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(str(shortcut_path))

# Set the target to run python in CMD with the updater.py and app.py
shortcut.Targetpath = "cmd.exe"
shortcut.Arguments = f'/k python "{target_folder / "updater.py"}" && python "{app_script_path}"'
shortcut.WorkingDirectory = str(target_folder)

# Use default .exe icon (shell32.dll index 2)
shortcut.IconLocation = "C:\\Windows\\System32\\shell32.dll,2"

# Save the shortcut
shortcut.save()
print("Shortcut created on desktop.")
