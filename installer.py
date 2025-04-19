import os
import shutil
import time
import urllib.request
from datetime import datetime
from urllib.request import urlretrieve

def create_folders_and_files():
    # Define the target directory for the app installation
    user_documents = os.path.expanduser("~\\Documents")
    nova_app_folder = os.path.join(user_documents, "NovaApp")
    assets_folder = os.path.join(nova_app_folder, "assets")
    backup_folder = os.path.join(nova_app_folder, "Backups")

    # Create necessary directories
    if not os.path.exists(nova_app_folder):
        os.makedirs(nova_app_folder)
    if not os.path.exists(assets_folder):
        os.makedirs(assets_folder)
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Download the icon and save it in the assets folder
    icon_url = "https://raw.githubusercontent.com/3rik11/nova/main/icon.ico"
    icon_path = os.path.join(assets_folder, "icon.ico")
    download_icon(icon_url, icon_path)

    # Define the path to save the app.py
    app_file_path = os.path.join(nova_app_folder, "app.py")

    # Sample app.py content (replace with actual content or load from file)
    app_content = """[PASTE APP.PY CONTENT HERE]"""

    # Write app.py content to the file
    with open(app_file_path, 'w') as app_file:
        app_file.write(app_content)

    # Backup the app.py file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_path = os.path.join(backup_folder, f"app_backup_{timestamp}.py")
    shutil.copy2(app_file_path, backup_file_path)

    print(f"App installed at {app_file_path}")
    print(f"Backup created at {backup_file_path}")

    # Create a Windows shortcut on Desktop to run app.py
    create_shortcut_on_desktop(app_file_path, icon_path)

def download_icon(url, path):
    """Download the icon from the given URL and save it to the specified path"""
    try:
        urlretrieve(url, path)
        print(f"Icon downloaded to {path}")
    except Exception as e:
        print(f"Failed to download icon: {e}")

def create_shortcut_on_desktop(app_file_path, icon_path):
    # Define the shortcut path
    desktop_path = os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"))
    shortcut_path = os.path.join(desktop_path, "NOVA Assistant.lnk")

    # Define the command to run the app.py (in CMD) and set the icon for the CMD window
    target = "cmd.exe"
    arguments = f"/K python \"{app_file_path}\""  # Run app.py using cmd
    icon = icon_path  # Use the downloaded icon for the shortcut and CMD window

    # Create a Windows shortcut (.lnk) using the 'os' module or pywin32 library
    try:
        import win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = target
        shortcut.Arguments = arguments
        shortcut.IconLocation = icon
        shortcut.save()
        print(f"Shortcut created at {shortcut_path}")
    except ImportError:
        print("Error creating shortcut. Please install pywin32 using 'pip install pywin32'")

if __name__ == "__main__":
    create_folders_and_files()
