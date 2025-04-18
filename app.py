import urllib.request
import time
import random
import os
import sys
import shutil
import platform
from datetime import datetime, date
import ast
import webbrowser
import requests
def update_file_from_github(raw_url):
    """
    Replaces the contents of the current file with the contents of a file from a GitHub raw URL,
    creating a backup first in the 'Backups' folder.
    """
    try:
        # Define the backup folder path
        user_documents = os.path.expanduser("~\\Documents")
        nova_app_folder = os.path.join(user_documents, "NovaApp")
        backup_folder = os.path.join(nova_app_folder, "Backups")

        # Ensure the backup folder exists
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        # Get the current file path
        current_file_path = os.path.abspath(__file__)

        # Download the new content from GitHub
        response = urllib.request.urlopen(raw_url)
        new_content = response.read().decode('utf-8')

        # Create a backup with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file_path = os.path.join(backup_folder, f"app_backup_{timestamp}.py")
        shutil.copy2(current_file_path, backup_file_path)

        # Write new content to the current file
        with open(current_file_path, 'w', encoding='utf-8') as current_file:
            current_file.write(new_content)

        print(f"✅ File successfully updated from GitHub. Backup created at: {backup_file_path}")
    except Exception as e:
        print(f"❌ Update failed: {e}")

# Run the update function on startup
github_raw_url = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"  # Replace with your raw URL
update_file_from_github(github_raw_url)
VERSION = "v1.3.9"
os.system('color A')
print(f"N.O.V.A. {VERSION}")
time.sleep(2)

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        response = requests.get(url)
        data = response.json()
        if data["error"]:
            return "Sorry, I couldn't fetch a joke right now."
        return data["joke"]
    except Exception as e:
        return f"Oops! Something went wrong: {e}"

def clear_backups(backup_folder):
    """
    Deletes all files in the backup folder older than 7 days.
    """
    try:
        now = time.time()
        for filename in os.listdir(backup_folder):
            file_path = os.path.join(backup_folder, filename)
            if os.path.isfile(file_path) and (now - os.path.getmtime(file_path)) > 7 * 86400:
                os.remove(file_path)
                print(f"Deleted old backup: {file_path}")
    except Exception as e:
        print(f"Error clearing backups: {e}")

def safe_eval(expr):
    try:
        # Only evaluate safe math expressions
        tree = ast.parse(expr, mode='eval')
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp,
                                     ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
                                     ast.Mod, ast.FloorDiv, ast.USub, ast.Constant)):
                raise ValueError("Unsafe expression")
        return eval(compile(tree, "<string>", mode="eval"))
    except Exception as e:
        return f"Error: {e}"



today = date.today()

# N.O.V.A. – Neural Operations Virtual Assistant

def type(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to next line after finishing

def typein(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_if_birthday(dob, space=1):
    try:
        dob_dt = datetime.strptime(dob, "%d-%m-%Y")
        if dob_dt.day == today.day and dob_dt.month == today.month:
            if space == 1:
                message = " 🎉 HAPPY BIRTHDAY!"
            elif space == 0:
                message = "🎉 HAPPY BIRTHDAY!"
            return str(message), 1  # 1 indicates it's the user's birthday
        else:
            return "", 0  # 0 indicates it's not their birthday
    except ValueError:
        return " (Invalid date format. Use DD-MM-YYYY)", 0

def novaintro(name, dob):
    birthday_msg, birthday = check_if_birthday(dob, space=1)
    if birthday == 1:
        type("WELCOME TO N.O.V.A. " + name + birthday_msg, 0.05)
    type("WELCOME TO N.O.V.A. " + name, 0.05)
    time.sleep(1)
    clear()
    type("IS THIS YOUR FIRST TIME USING N.O.V.A.?", 0.05)
    typein("Y/N ", 0.05)
    first_time = input().upper()
    if first_time == "Y":
        clear()
        type("Thank you for choosing Nova, Nova is a very useful AI to keep you entertained and for general productivity. At any time, just type help to get a full list of all commands you can ask Nova.", 0.05)
        time.sleep(5)
        clear()
        nova(name, dob, first_time)
    elif first_time == "N":
        clear()
        type("WELCOME BACK, " + name, 0.05)
        nova(name, dob, first_time)

def nova(name, dob, first_time):
    clear()
    running = True
    firsttime = True

    birthday_msg, birthday = check_if_birthday(dob, space=0)
    if birthday == 1:
        type(birthday_msg, 0.05)
    elif birthday == 0 and first_time == "N":
        type("WELCOME BACK, " + name, 0.05)
    elif birthday == 0 and first_time == "Y":
        type("WELCOME TO N.O.V.A, " + name, 0.05)

    while running:
        if firsttime:
            type("TYPE HELP FOR A LIST OF COMMANDS", 0.05)
            firsttime = False
        else:
            type("TYPE HELP FOR A LIST OF COMMANDS", 0.03)
            
        typein(">>> ", 0.05)
        command = input().lower()
        if command == "help":
            clear()
            type("COMMANDS:", 0.02)
            type("1. help - Displays this help message.", 0.02)
            type("2. date - Displays the current date.", 0.02)
            type("3. time - Displays the current time.", 0.02)
            type("4. exit - Exits the program.", 0.02)
            type("5. clear - Clears the screen.", 0.02)
            type("6. calculator - Plays a rick roll!.", 0.02)
            type("7. math - A real calculator.", 0.02)
            type("8. color - Change the color of the terminal.", 0.02)
            type("9. reboot - Reboots N.O.V.A.", 0.02)
            type("10. signin - Ask me for a unique password that stores all of your details so you dont have to enter them every time you login.", 0.02)
            type("11. clearbackups - Clears all backups older than 7 days.", 0.02)
            type("12. joke - Shows a joke.", 0.02)
            time.sleep(2)
            clear()
        elif command == "joke":
            clear()
            joke = get_joke()
            type(joke, 0.05)
            input("Press Enter to continue...")
            clear()
        elif command == "clearbackups":
            clear_backups(os.path.join(os.path.expanduser("~\\Documents"), "NovaApp", "Backups"))
            type("BACKUPS CLEARED", 0.05)
            time.sleep(0.5)
            clear()
        elif command == "signin":
            URL = "3rik11.github.io/nova/from.html"
            type("REDIRECTING TO FORM WEBSITE", 0.05)
            time.sleep(2)
            webbrowser.open(URL)
            input("Press Enter to continue...")
            clear()
        elif command == "reboot":
            if os.name == 'nt':
                user = os.getlogin()
                os.system(fr'start cmd /k "cd /d C:\Users\{user}\Documents\NovaApp && python app.py"')
                os.system('exit')
                break
            else:
                os.system(f'python3 "{os.path.abspath(__file__)}" &')
                exit()
        elif command == "color":
            if os.name == 'nt':
                colors = [
                    "0 = Black", "1 = Blue", "2 = Green", "3 = Aqua",
                    "4 = Red", "5 = Purple", "6 = Yellow", "7 = White",
                    "8 = Gray", "9 = Light Blue", "A = Light Green", "B = Light Aqua",
                    "C = Light Red", "D = Light Purple", "E = Light Yellow", "F = Bright White"
                ]
                for color in colors:
                    type(color, 0.02)
                type("PLEASE ENTER YOUR COLOR CHOICE ", 0.02)
                typein(">>> ", 0.05)
                color_choice = input().upper()
                if color_choice in "0123456789ABCDEF":
                    os.system(f'color {color_choice}')
                    clear()
            else:
                type("Color customization not supported on this OS.", 0.05)
                time.sleep(2)
                clear()
        elif command == "date":
            clear()
            type("TODAY'S DATE: " + str(today), 0.05)
            time.sleep(2)
            clear()
        elif command == "time":
            clear()
            type("CURRENT TIME: " + datetime.now().strftime("%H:%M:%S"), 0.05)
            time.sleep(2)
            clear()
        elif command == "exit":
            clear()
            type("GOODBYE, " + name, 0.05)
            os.system('exit')
        elif command == "clear":
            clear()
        elif command == "calculator":
            cmdvar = os.system('curl ASCII.live/can-you-hear-me')
            print(cmdvar)
        elif command.startswith("math "):
            expression = command[5:]
            result = safe_eval(expression)
            type (f"RESULT: {result}", 0.05)
        else:
            clear()
            type("UNKNOWN COMMAND", 0.05)
            time.sleep(1)
            clear()
    time.sleep(1)
    clear()



clear()
type("WELCOME TO NEURAL OPERATIONS VIRTUAL ASSISTANT, ALSO KNOWN AS N.O.V.A.", 0.05)
time.sleep(0.3)
clear()
type("WOULD YOU LIKE TO CONTINUE AS A GUEST USER?", 0.05)
typein("Y/N ", 0.05)
user_choise = input().upper()
if user_choise == "Y":
    clear()
    type("WELCOME, GUEST USER", 0.05)
    time.sleep(0.3)
    clear()
    type("SETUP FOR GUEST USER ACTIVATED", 0.05)
    time.sleep(0.3)
    clear()
    typein("PLEASE ENTER YOUR NAME: ", 0.05)
    namelower = str(input())
    name = namelower.upper()
    clear()
    typein("PLEASE ENTER YOUR DATE OF BIRTH (DD-MM-YYYY): ", 0.05)
    dob = input()
    clear()
    novaintro(name, dob)
elif user_choise == "N":
    clear()
    type("PLEASE ENTER USER AUTHENTICATION CODE", 0.05)
    typein(">>> ", 0.05)
    authcode = input()
    type("VERIFYING AUTHENTICATION CODE", 0.05)
    time.sleep(1)
    clear()
    if authcode == "ADMIN":
        nova("ADMIN", "25-07-2014", first_time="N")
    else:
        type("INVALID AUTHENTICATION CODE", 0.05)
        time.sleep(2)
        clear()
        type("SHUTTING DOWN APPLICATION", 0.05)
        time.sleep(2)
        clear()
        exit()
elif user_choise == "FAST":
    nova("ADMIN", "25-07-2014", first_time="N")
else:
    clear()
    type("INVALID INPUT", 0.05)
    time.sleep(2)
    clear()
    type("SHUTTING DOWN APPLICATION", 0.05)
    time.sleep(2)
    clear()
    exit()
