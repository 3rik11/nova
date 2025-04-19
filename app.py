import urllib.request
import time
import random
import os
import sys
import shutil
import platform
from datetime import datetime, date
import ast
import subprocess
VERSION = "v1.1.0"

print(f"N.O.V.A. Assistant – {VERSION}")
time.sleep(0.5)

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


def update_file_from_github(raw_url):
    """
    Replaces the contents of the current file with the contents of a file from a GitHub raw URL,
    creating a backup first.
    """
    try:
        response = urllib.request.urlopen(raw_url)
        new_content = response.read().decode('utf-8')

        current_file_path = os.path.abspath(__file__)
        backup_path = current_file_path + ".bak"

        # Backup current script
        shutil.copy2(current_file_path, backup_path)

        # Write new content
        with open(current_file_path, 'w', encoding='utf-8') as current_file:
            current_file.write(new_content)

        print("✅ File successfully updated from GitHub. Backup created at:", backup_path)
    except Exception as e:
        print(f"❌ Update failed: {e}")

# Run the update function on startup
github_raw_url = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"  # Replace with your raw URL
update_file_from_github(github_raw_url)

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
            time.sleep(2)
            clear()
        elif command == "reboot":
            if os.name == 'nt':
                user = os.getlogin()
                os.system(fr'start cmd /k "cd /d C:\Users\{user}\Documents\Python\Getting Started && python app.py"')
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
            running = False
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
    firsttime = 0



# def boot_sequence():
#     lines = [
#         "[ OK ] Initializing nova-Core v3.7.29",
#         "[ OK ] Loading ROM memory sectors",
#         "[ OK ] Establishing internal kernel interfaces",
#         "[ OK ] Mounting /dev/null.exe",
#         "[ OK ] Syncing time server @ 127.0.0.1.99:1400",
#         "[ OK ] Checking quantum loopback",
#         "[ OK ] Activating neural input grid",
#         "[WARN] Entropy below threshold, reseeding...",
#         "[ OK ] Bootstrapping hypervisor",
#         "[ OK ] Loading modules: ui, net, core, shell",
#         "[FAIL] Unable to load module 'coffee-maker'",
#         "[ OK ] Establishing connection to host shell",
#         "[ OK ] Injecting personality core",
#         "[ OK ] System entropy nominal",
#         "[ OK ] Boot complete. Welcome, Operator.",
#     ]

#     for line in lines:
#         time.sleep(random.uniform(0.05, 0.15))
#         print(line)

# def matrix_rain(duration=3):
#     chars = "01█▓▒░<>/"
#     end_time = time.time() + duration
#     columns = 80

#     while time.time() < end_time:
#         line = ''.join(random.choice(chars) for _ in range(columns))
#         print(line)
#         time.sleep(0.05)

# def main():
#     clear()
#     matrix_rain(2)
#     print("\n>>> SYSTEM BOOTING...\n")
#     time.sleep(1)
#     boot_sequence()
#     print("\n>>> nova-core ready. Launching interface...\n")
#     time.sleep(5)
#     matrix_rain(2)

# if __name__ == "__main__":
#     main()



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
        novaintro("ADMIN", "25-07-2014")
    else:
        type("INVALID AUTHENTICATION CODE", 0.05)
        time.sleep(2)
        clear()
        type("SHUTTING DOWN APPLICATION", 0.05)
        time.sleep(2)
        clear()
        exit()
else:
    clear()
    type("INVALID INPUT", 0.05)
    time.sleep(2)
    clear()
    type("SHUTTING DOWN APPLICATION", 0.05)
    time.sleep(2)
    clear()
    exit()