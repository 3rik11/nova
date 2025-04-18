import urllib.request
import time
import random
import os
import sys
from datetime import datetime, date

today = date.today()

# N.O.V.A. – Neural Operations Virtual Assistant

def check_for_update():
    remote_url = "https://raw.githubusercontent.com/3rik11/nova/main/app.py"
    local_file = os.path.realpath(__file__)

    try:
        with urllib.request.urlopen(remote_url) as response:
            remote_code = response.read()

        with open(local_file, "rb") as local:
            local_code = local.read()

        if remote_code != local_code:
            print("[UPDATE] New version found! Updating...")
            time.sleep(3)
            with open(local_file, "wb") as f:
                f.write(remote_code)
            print("[UPDATE] Update complete. Please restart the app.")
            time.sleep(10)
            exit()
        else:
            print("[OK] App is up to date.")
            time.sleep(1)
    except Exception as e:
        print(f"[ERROR] Failed to check for updates: {e}")
        time.sleep(3)

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
            # Return an empty string and a flag of 0 if it's not their birthday
            return "", 0  # 0 indicates it's not their birthday
    except ValueError:
        # If the date format is invalid, return an error message and flag 0
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
    firsttime = 1
    birthday_msg, birthday = check_if_birthday(dob, space=0)
    if birthday == 1:
        type(birthday_msg, 0.05)
    elif birthday == 0 and first_time == "N":
        type("WELCOME " + name, 0.05)
    while True:       
        if firsttime == 1:          
            type("TYPE HELP FOR A LIST OF COMMANDS", 0.05)
            typein(">>> ", 0.05)
            command = input().lower()
        elif firsttime == 0:
            type("TYPE HELP FOR A LIST OF COMMANDS", 0.03)
            typein(">>> ", 0.05)
            command = input().lower()
            firsttime = 0
        if command == "help":
            clear()
            type("COMMANDS:", 0.02)
            type("1. help - Displays this help message.", 0.02)
            type("2. date - Displays the current date.", 0.02)
            type("3. time - Displays the current time.", 0.02)
            type("4. exit - Exits the program.", 0.02)
            type("5. clear - Clears the screen.", 0.02)
            type("5. calculator - Plays a rick roll!.", 0.02)
            type("6. math - A real calculator.", 0.02)
            type("7. color - Change the color of the terminal.", 0.02)
            type("8. reboot - Reboots N.O.V.A.", 0.02)
            time.sleep(2)
            clear()
        elif command == "reboot":
            user = os.getlogin()
            os.system(fr'start cmd /k "cd /d C:\Users\{user}\Documents\Python\Getting Started && python app.py"')
            exit()
        elif command == "color":
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
            exit()
        elif command == "clear":
            clear()
        elif command == "calculator":
            # curl ASCII.live/can-you-hear-me
            cmdvar = os.system('curl ASCII.live/can-you-hear-me')
            print(cmdvar)
        elif command == "math":
            clear()
            type("WELCOME TO N.O.V.A. CALCULATOR", 0.05)
            type("PLEASE ENTER YOUR CALCULATION: ", 0.05)
            typein(">>> ", 0.05)
            calc = input()
            try:
                result = eval(calc)
                clear()
                type("RESULT: " + str(result), 0.05)
            except Exception as e:
                clear()
                type("ERROR: " + str(e), 0.05)
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
check_for_update()
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
        type("SHUTTING DOWN APPLIACTION", 0.05)
        time.sleep(2)
        clear()
        exit()
else:
    clear()
    type("INVALID INPUT", 0.05)
    time.sleep(2)
    clear()
    type("SHUTTING DOWN APPLIACTION", 0.05)
    time.sleep(2)
    clear()
    exit()       