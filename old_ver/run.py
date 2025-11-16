import os
import requests
import subprocess
from datetime import datetime, timedelta

# Paths and URLs
local_dir = os.path.join(os.getenv('USERPROFILE'), "Documents", "NovaApp")  # Ensure correct path for Windows
backup_dir = os.path.join(local_dir, "Backups")
local_version_path = os.path.join(local_dir, "version.vrsn")
local_app_path = os.path.join(local_dir, "app.py")
remote_version_url = "https://3rik11.gituhb.io/nova/version.md"
remote_app_url = "https://raw.githubusercontent.com/3rik11/nova/refs/heads/main/app.py"

def run_app():
    try:
        subprocess.run(["python", local_app_path], check=True)
    except Exception as e:
        print(f"Failed to run app.py: {e}")

def create_backup():
    # Do not create the backup directory; assume it already exists.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"app_{timestamp}.py"
    backup_path = os.path.join(backup_dir, backup_filename)

    try:
        with open(local_app_path, 'r', encoding='utf-8') as original_file:
            content = original_file.read()
        with open(backup_path, 'w', encoding='utf-8') as backup_file:
            backup_file.write(content)
        print(f"Backed up app.py to {backup_filename}")
    except Exception as e:
        print(f"Failed to create backup: {e}")

def cleanup_old_backups():
    # Get the current time and the time threshold (7 days ago)
    now = datetime.now()
    threshold = now - timedelta(days=7)

    # Check each file in the Backups directory
    for backup_file in os.listdir(backup_dir):
        backup_path = os.path.join(backup_dir, backup_file)

        if os.path.isfile(backup_path):
            # Get the file's last modified time
            file_time = datetime.fromtimestamp(os.path.getmtime(backup_path))

            # If the file is older than 7 days, delete it
            if file_time < threshold:
                try:
                    os.remove(backup_path)
                    print(f"Deleted old backup: {backup_file}")
                except Exception as e:
                    print(f"Error deleting backup {backup_file}: {e}")

try:
    # Cleanup old backups (older than 7 days)
    cleanup_old_backups()

    # Read local version
    with open(local_version_path, 'r', encoding='utf-8') as file:
        local_version = file.read().strip().lower()

    # Fetch remote version
    response = requests.get(remote_version_url)
    response.raise_for_status()
    remote_version = response.text.strip().lower()

    # Compare versions
    if local_version != remote_version:
        print("Version mismatch detected. Updating app.py...")

        # Backup current app.py
        if os.path.exists(local_app_path):
            create_backup()
            os.remove(local_app_path)
            print("Deleted old app.py")

        # Download and save new app.py
        response = requests.get(remote_app_url)
        response.raise_for_status()
        with open(local_app_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print("Downloaded new app.py")

        version_file_path = os.path.join(os.path.expanduser("~"), "Documents", "NovaApp", "version.vrsn")
        try:
            os.makedirs(os.path.dirname(version_file_path), exist_ok=True)  # Make sure the directory exists
            with open(version_file_path, "w") as version_file:
                version_file.write(remote_version)
        except Exception as e:
            print(f"Failed to write version file: {e}")

        # Update the version file
        with open(local_version_path, 'w', encoding='utf-8') as file:
            file.write(remote_version)

    else:
        print("Version is up-to-date.")

    # Run the app
    run_app()

except Exception as e:
    print(f"Error occurred: {e}")
