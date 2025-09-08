import json
import os

HOMEWORK_FILE = "data/homework.json"

def load_homework():
    if not os.path.exists(HOMEWORK_FILE) or os.stat(HOMEWORK_FILE).st_size == 0:
        with open(HOMEWORK_FILE, "w") as f:
            f.write("[]")
    with open(HOMEWORK_FILE, "r") as f:
        return json.load(f)

def save_homework(homework_tasks):
    with open(HOMEWORK_FILE, "w") as f:
        json.dump(homework_tasks, f, indent=4)

def add_homework():
    homework_tasks = load_homework()
    
    while True:
        subject = input("Enter subject: ").strip()
        if subject and not subject.isdigit():
            break
        print("Please enter a valid subject name (words, not numbers).")
    
    while True:
        task = input("Enter homework task: ").strip()
        if task and not task.isdigit():
            break
        print("Please enter a valid homework task (words, not numbers).")
    
    homework_tasks.append({"subject": subject, "task": task})
    save_homework(homework_tasks)
    print(f"Added homework for {subject}: {task}")

def view_homework():
    homework_tasks = load_homework()
    if homework_tasks:
        print("\nHomework Tasks:")
        for h in homework_tasks:
            print(f"- {h['subject']}: {h['task']}")
    else:
        print("No homework tasks yet.")
