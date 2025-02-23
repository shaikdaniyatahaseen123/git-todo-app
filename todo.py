# todo.py - A simple command-line To-Do App

tasks = []  # List to store tasks

def add_task(task):
    """Adds a new task to the list."""
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    """Displays all tasks."""
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour To-Do List is empty.")

def remove_task(index):
    """Removes a task by its number."""
    try:
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' removed!")
    except IndexError:
        print("Invalid task number.")

def main():
    """Main function to run the To-Do App."""
    while True:
        print("\n==== To-Do App ====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
