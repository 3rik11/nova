import os
import datetime
import urllib.request
import shutil
import subprocess
import sys
def update_app_py_from_github(raw_url):
    """
    Downloads app.py from a GitHub raw URL and replaces the existing app.py in the NovaApp folder,
    creating a timestamped backup in the Backups folder. Then opens the app.py file in a new command prompt.
    """
    try:
        # Define paths
        user_documents = os.path.expanduser("~\\Documents")
        nova_app_folder = os.path.join(user_documents, "NovaApp")
        app_file_path = os.path.join(nova_app_folder, "app.py")
        backup_folder = os.path.join(nova_app_folder, "Backups")

        # Ensure backup directory exists
        os.makedirs(backup_folder, exist_ok=True)

        # Download new app.py content
        response = urllib.request.urlopen(raw_url)
        new_content = response.read().decode('utf-8')

        # Backup current app.py
        if os.path.exists(app_file_path):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file_path = os.path.join(backup_folder, f"app_backup_{timestamp}.py")
            shutil.copy2(app_file_path, backup_file_path)
            print(f"🔒 Backup of existing app.py saved to: {backup_file_path}")

        # Write new content to app.py
        with open(app_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ app.py has been successfully updated from GitHub.")

        # Open the updated app.py in a new command prompt (cmd)
        cmd_command = f"start cmd.exe /K python \"{app_file_path}\""
        os.system(cmd_command)
    except Exception as e:
        print(f"❌ Update failed: {e}")


if __name__ == "__main__":
    # Example raw URL of the updated app.py file
    GITHUB_RAW_URL = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"
    update_app_py_from_github(GITHUB_RAW_URL)
    sys.exit()
