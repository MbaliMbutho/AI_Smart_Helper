import json
import os
import re

CHORES_FILE = "data/chores.json"

def load_chores():
    if not os.path.exists(CHORES_FILE) or os.stat(CHORES_FILE).st_size == 0:
        with open(CHORES_FILE, "w") as f:
            f.write("[]")
    with open(CHORES_FILE, "r") as f:
        return json.load(f)

def save_chores(chores):
    with open(CHORES_FILE, "w") as f:
        json.dump(chores, f, indent=4)

def add_chore():
    chores = load_chores()
    
    while True:
        task = input("Enter the chore: ").strip()
        if task and not task.isdigit():
            break
        print("Please enter a valid chore name (words, not numbers).")
    
    while True:
        time = input("Enter time (HH:MM, 24-hour format): ").strip()
        if re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", time):
            break
        print("Please enter a valid time in HH:MM format.")
    
    chores.append({"task": task, "time": time})
    save_chores(chores)
    print(f"Chore '{task}' added for {time}.")

def view_chores():
    chores = load_chores()
    if chores:
        print("\nToday's chores:")
        for c in chores:
            print(f"- {c['task']} at {c['time']}")
    else:
        print("No chores added yet.")

