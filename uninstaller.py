import os
import shutil
import sys
from pathlib import Path
import subprocess

def uninstall_libraries():
    libraries_to_uninstall = ["pywin32", "requests"]

    for lib in libraries_to_uninstall:
        try:
            # Try to import the library
            __import__(lib)
            print(f"Uninstalling {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", lib])
        except ImportError:
            # If library is already uninstalled, skip it
            print(f"{lib} is not installed, skipping uninstallation.")

def delete_folder(folder_path):
    """Deletes the folder and all its contents."""
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"✅ Successfully deleted the folder: {folder_path}")
        else:
            print(f"❌ Folder not found: {folder_path}")
    except Exception as e:
        print(f"❌ Error deleting the folder: {e}")

def delete_shortcut():
    """Deletes the NovaApp shortcut from the desktop."""
    try:
        # Get the desktop path based on the OS
        if os.name == 'nt':  # Windows
            user_profile = os.environ.get("USERPROFILE")
            desktop_path = os.path.join(user_profile, "Desktop")
            shortcut_path = os.path.join(desktop_path, "NOVA Assistant.lnk")  # Correct shortcut name here
        else:  # For other operating systems, like macOS and Linux
            user_profile = os.environ.get("HOME")
            desktop_path = os.path.join(user_profile, "Desktop")
            shortcut_path = os.path.join(desktop_path, "NovaApp.desktop")
        
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
            print(f"✅ Successfully deleted the shortcut: {shortcut_path}")
        else:
            print(f"❌ Shortcut not found: {shortcut_path}")
    except Exception as e:
        print(f"❌ Error deleting the shortcut: {e}")

def uninstall():
    """Handles the uninstallation process."""
    try:
        # Get the NovaApp directory path
        user_documents = os.path.expanduser("~\\Documents")
        nova_app_folder = os.path.join(user_documents, "NovaApp")

        # Delete the NovaApp folder and its contents
        delete_folder(nova_app_folder)

        # Delete the shortcut from the desktop
        delete_shortcut()

        # Uninstall the libraries
        uninstall_libraries()

        print("✅ Uninstallation completed successfully.")
    except Exception as e:
        print(f"❌ Error during uninstallation: {e}")

# Run the uninstaller
if __name__ == "__main__":
    os.system("color A")
    confirm_uninstall = input("Are you sure you want to uninstall NovaApp and delete all its contents? (Y/N): ").upper()
    if confirm_uninstall == "Y":
        uninstall()
    else:
        print("❌ Uninstallation aborted.")
