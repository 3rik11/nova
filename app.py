import time
import os
import random 
def type(text, speed):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed)
    print()

def typein(text, speed):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_version():
    with open("version.vrsn", "r") as version_file:
        version = version_file.read().strip()
    return version

def startup():
    type("NOVA VRSN: " + load_version(), 0.05)
    time.sleep(1)
    clear()
    load = 0
    while load < 5:
        if load == 0:
            type("Starting NOVA.", 0.05)
            time.sleep(random.uniform(0.5, 1.5))
            clear()
        else:
            print("Starting NOVA.")
            time.sleep(random.uniform(0.5, 1.5))
            clear()
        print("Starting NOVA..")
        time.sleep(random.uniform(0.5, 1.5))
        clear()
        print("Starting NOVA...")
        time.sleep(random.uniform(0.5, 1.5))
        clear()
        print("Starting NOVA....")
        time.sleep(random.uniform(0.5, 1.5))
        clear()
        print("Starting NOVA.....")
        time.sleep(random.uniform(0.5, 1.5))
        clear()
        load += 1
    clear()

    



startup()

