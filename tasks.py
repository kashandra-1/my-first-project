import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid number!")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Show tasks\n2. Add task\n3. Delete task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()