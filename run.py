import os
import requests
import subprocess

# Paths and URLs
local_dir = os.path.expanduser("~/Documents/NovaApp")
local_version_path = os.path.join(local_dir, "version.txt")
local_app_path = os.path.join(local_dir, "app.py")
remote_version_url = "https://3rik11.gituhb.io/nova/version.md"
remote_app_url = "https://raw.githubusercontent.com/3rik11/nova/refs/heads/main/app.py"

def run_app():
    try:
        subprocess.run(["python", local_app_path], check=True)
    except Exception as e:
        print(f"Failed to run app.py: {e}")

try:
    # Read local version
    with open(local_version_path, 'r') as file:
        local_version = file.read().strip()

    # Fetch remote version
    response = requests.get(remote_version_url)
    response.raise_for_status()
    remote_version = response.text.strip()

    # Compare versions
    if local_version != remote_version:
        print("Version mismatch detected. Updating app.py...")

        # Delete old app.py if exists
        if os.path.exists(local_app_path):
            os.remove(local_app_path)
            print("Deleted old app.py")

        # Download and save new app.py
        response = requests.get(remote_app_url)
        response.raise_for_status()
        with open(local_app_path, 'w') as file:
            file.write(response.text)
        print("Downloaded new app.py")

        # Optionally update the version.txt
        with open(local_version_path, 'w') as file:
            file.write(remote_version)

    else:
        print("Version is up-to-date.")

    # Run the app
    run_app()

except Exception as e:
    print(f"Error occurred: {e}")
