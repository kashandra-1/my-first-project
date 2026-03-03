import json
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8", errors="ignore") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def show_tasks(tasks):
    if not tasks:
        console.print("[bold red]No tasks yet![/bold red]")
        return

    table = Table(title="📋 Your Tasks", box=box.ROUNDED)
    table.add_column("#", style="cyan")
    table.add_column("Status")
    table.add_column("Priority")
    table.add_column("Title", style="white")
    table.add_column("Created")

    for i, task in enumerate(tasks, 1):
        status = "[green]✅ Done[/green]" if task["done"] else "[red]❌ Todo[/red]"

        priority_color = {
            "low": "green",
            "medium": "yellow",
            "high": "red"
        }.get(task["priority"], "white")

        priority = f"[{priority_color}]{task['priority'].upper()}[/{priority_color}]"

        table.add_row(
            str(i),
            status,
            priority,
            task["title"],
            task["created_at"]
        )

    console.print(table)


def clean_text(text):
    return text.encode("utf-8", "ignore").decode("utf-8")


def add_task(tasks):
    title = input("Task title: ").strip()
    title = clean_text(title)

    priority = input("Priority (low/medium/high): ").strip().lower()

    if priority not in ["low", "medium", "high"]:
        console.print("[yellow]Invalid priority! Setting to medium.[/yellow]")
        priority = "medium"

    task = {
        "title": title,
        "done": False,
        "priority": priority,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    tasks.append(task)
    save_tasks(tasks)
    console.print("[bold green]Task added![/bold green]")


def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: ").strip())
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        console.print("[green]Marked as done![/green]")
    except (ValueError, IndexError):
        console.print("[red]Invalid number![/red]")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ").strip())
        tasks.pop(num - 1)
        save_tasks(tasks)
        console.print("[red]Task deleted![/red]")
    except (ValueError, IndexError):
        console.print("[red]Invalid number![/red]")


def main():
    tasks = load_tasks()

    while True:
        console.print("\n[bold cyan]1.[/bold cyan] Show tasks")
        console.print("[bold cyan]2.[/bold cyan] Add task")
        console.print("[bold cyan]3.[/bold cyan] Mark as done")
        console.print("[bold cyan]4.[/bold cyan] Delete task")
        console.print("[bold cyan]5.[/bold cyan] Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            console.print("[red]Invalid choice![/red]")


if __name__ == "__main__":
    main()