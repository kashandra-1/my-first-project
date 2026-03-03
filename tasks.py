import json
import os
from datetime import datetime

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
        return

    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} [{task['priority']}] {task['title']} (created: {task['created_at']})")

def add_task(tasks):
    title = input("Task title: ")
    priority = input("Priority (low/medium/high): ").lower()

    if priority not in ["low", "medium", "high"]:
        print("Invalid priority! Setting to medium.")
        priority = "medium"

    task = {
        "title": title,
        "done": False,
        "priority": priority,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Marked as done!")
    except (ValueError, IndexError):
        print("Invalid number!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted!")
    except (ValueError, IndexError):
        print("Invalid number!")

def filter_tasks(tasks):
    priority = input("Filter by priority (low/medium/high): ").lower()
    filtered = [t for t in tasks if t["priority"] == priority]
    show_tasks(filtered)

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Mark as done")
        print("4. Delete task")
        print("5. Filter by priority")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            filter_tasks(tasks)
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()