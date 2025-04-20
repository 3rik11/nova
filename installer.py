import os
import shutil
import time
import urllib.request
from urllib.request import urlretrieve
import subprocess
import sys

# Function to ensure required libraries are installed
def install_required_libraries():
    required_libraries = ["pywin32", "requests"]
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            print(f"Installing {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

def create_folders_and_files():
    user_documents = os.path.expanduser("~\\Documents")
    nova_app_folder = os.path.join(user_documents, "NovaApp")
    assets_folder = os.path.join(nova_app_folder, "assets")

    os.makedirs(assets_folder, exist_ok=True)

    # Download and save icon
    icon_url = "https://raw.githubusercontent.com/3rik11/nova/refs/heads/main/icon.ico"
    icon_path = os.path.join(assets_folder, "icon.ico")
    download_icon(icon_url, icon_path)

    # Download app.py
    app_url = "https://raw.githubusercontent.com/3rik11/nova/refs/heads/main/app.py"
    app_file_path = os.path.join(nova_app_folder, "app.py")
    download_file(app_url, app_file_path)

    # Download uninstaller.py
    uninstaller_url = "https://raw.githubusercontent.com/3rik11/nova/refs/heads/main/uninstaller.py"
    uninstaller_file_path = os.path.join(nova_app_folder, "uninstaller.py")
    download_file(uninstaller_url, uninstaller_file_path)

    print(f"\nFiles installed in {nova_app_folder}")

    # Create shortcut to run updater.py
    create_shortcut_on_desktop(app_file_path, icon_path)

def download_icon(url, path):
    try:
        urlretrieve(url, path)
        print(f"Icon downloaded to {path}")
    except Exception as e:
        print(f"Failed to download icon: {e}")

def download_file(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        print(f"Downloaded: {path}")
    except Exception as e:
        print(f"Failed to download file from {url}: {e}")

def create_shortcut_on_desktop(target_file, icon_path):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    shortcut_path = os.path.join(desktop_path, "NOVA Assistant.lnk")

    try:
        import win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = "cmd.exe"
        shortcut.Arguments = f'/K python "{target_file}"'
        shortcut.IconLocation = icon_path
        shortcut.save()
        print(f"Shortcut created at {shortcut_path}")
    except ImportError:
        print("Error creating shortcut. Please install pywin32 using 'pip install pywin32'")

if __name__ == "__main__":
    install_required_libraries()
    create_folders_and_files()
