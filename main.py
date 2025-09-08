from chores import add_chore, view_chores
from groceries import add_grocery, view_groceries
from homework import add_homework, view_homework

def main():
    while True:
        print("\n=== AI Smart Helper ===")
        print("1. Add Chore")
        print("2. View Chores")
        print("3. Add Grocery")
        print("4. View Groceries")
        print("5. Add Homework")
        print("6. View Homework")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_chore()
        elif choice == "2":
            view_chores()
        elif choice == "3":
            add_grocery()
        elif choice == "4":
            view_groceries()
        elif choice == "5":
            add_homework()
        elif choice == "6":
            view_homework()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
