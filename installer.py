import os
import shutil
import time
import urllib.request
from urllib.request import urlretrieve

def create_folders_and_files():
    # Define the target directory for the app installation
    user_documents = os.path.expanduser("~\\Documents")
    nova_app_folder = os.path.join(user_documents, "NovaApp")
    assets_folder = os.path.join(nova_app_folder, "assets")

    # Create necessary directories if they don't exist
    if not os.path.exists(nova_app_folder):
        os.makedirs(nova_app_folder)
    if not os.path.exists(assets_folder):
        os.makedirs(assets_folder)

    # Download the icon and save it in the assets folder
    icon_url = "https://raw.githubusercontent.com/3rik11/nova/main/icon.ico"
    icon_path = os.path.join(assets_folder, "icon.ico")
    download_icon(icon_url, icon_path)

    # Define the URL for app.py
    app_url = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"
    app_file_path = os.path.join(nova_app_folder, "app.py")

    # Download app.py content from the URL and save to the file
    download_file(app_url, app_file_path)

    print(f"App installed at {app_file_path}")

    # Create a Windows shortcut on Desktop to run app.py
    create_shortcut_on_desktop(app_file_path, icon_path)

def download_icon(url, path):
    """Download the icon from the given URL and save it to the specified path"""
    try:
        urlretrieve(url, path)
        print(f"Icon downloaded to {path}")
    except Exception as e:
        print(f"Failed to download icon: {e}")

def download_file(url, path):
    """Download a file from a URL and save it to the specified path"""
    try:
        urllib.request.urlretrieve(url, path)
        print(f"File downloaded from {url} to {path}")
