import sys
import csv
import os

CSV_FILE = "tasks.csv"
FIELDNAMES = ["id", "title", "completed"]


def ensure_csv_exists():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_task(task_id, title):
    """Add a new task with the given ID and title."""
    ensure_csv_exists()
    task = {"id": task_id, "title": title, "completed": "False"}
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(task)
    print(f"Task added: {title}")
    list_tasks()


def list_tasks():
    """Display all tasks from the CSV file."""
    ensure_csv_exists()
    tasks = []  # modified for flask
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)   # modified for flask
    return tasks    # modified for flask

def complete_task(task_id):
    """Mark a specific task as completed."""
    ensure_csv_exists()
    rows = []
    found = False

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == task_id:
                row["completed"] = "True"
                found = True
            rows.append(row)

    if found:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Task {task_id} marked as completed.")
    else:
        print(f"Task ID {task_id} not found.")

    list_tasks()


def delete_task(task_id):
    """Delete a task by its ID."""
    ensure_csv_exists()
    rows = []
    deleted = False

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] != task_id:
                rows.append(row)
            else:
                deleted = True

    if deleted:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task ID {task_id} not found.")

    list_tasks()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python task_tracker.py add <task_id> <title>")
        print("  python task_tracker.py complete <task_id>")
        print("  python task_tracker.py delete <task_id>")
        print("  python task_tracker.py list")
        sys.exit(1)

    action = sys.argv[1]

    if action == "list":
        list_tasks()

    elif action == "add":
        if len(sys.argv) < 4:
            print("Usage: python task_tracker.py add <task_id> <title>")
            sys.exit(1)
        task_id = sys.argv[2]
        title = " ".join(sys.argv[3:])
        add_task(task_id, title)

    elif action == "complete":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py complete <task_id>")
            sys.exit(1)
        task_id = sys.argv[2]
        complete_task(task_id)

    elif action == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py delete <task_id>")
            sys.exit(1)
        task_id = sys.argv[2]
        delete_task(task_id)

    else:
        print(f"Unknown command: {action}")
        print("Try: add, complete, delete, or list")