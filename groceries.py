# groceries.py
import json
import os

GROCERY_FILE = "data/groceries.json"

def load_groceries():
    if not os.path.exists(GROCERY_FILE) or os.stat(GROCERY_FILE).st_size == 0:
        with open(GROCERY_FILE, "w") as f:
            f.write("[]")
    with open(GROCERY_FILE, "r") as f:
        return json.load(f)

def save_groceries(groceries):
    with open(GROCERY_FILE, "w") as f:
        json.dump(groceries, f, indent=4)

def add_grocery():
    groceries = load_groceries()
    
    while True:
        item = input("Enter grocery item: ").strip()
        if item and not item.isdigit():  # grocery name should not be a number
            break
        print("Please enter a valid grocery name (words, not numbers).")
    
    groceries.append(item)
    save_groceries(groceries)
    print(f"Added '{item}' to groceries.")

def view_groceries():
    groceries = load_groceries()
    if groceries:
        print("\nGrocery List:")
        for g in groceries:
            print(f"- {g}")
    else:
        print("Grocery list is empty.")
