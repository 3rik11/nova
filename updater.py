import urllib.request
import os
import time

REMOTE_URL = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"
LOCAL_FILE = os.path.join(os.path.dirname(__file__), "app.py")

def update_app():
    try:
        with urllib.request.urlopen(REMOTE_URL) as response:
            remote_code = response.read()

        with open(LOCAL_FILE, "rb") as local:
            local_code = local.read()

        if remote_code != local_code:
            print("[UPDATE] New version found! Updating...")
            time.sleep(2)
            with open(LOCAL_FILE, "wb") as f:
                f.write(remote_code)
            print("[UPDATE] Update complete.")
        else:
            print("[OK] App is up to date.")
    except Exception as e:
        print(f"[ERROR] Could not update: {e}")

update_app()
