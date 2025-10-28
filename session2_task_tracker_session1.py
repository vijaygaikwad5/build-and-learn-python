import sys  # for sys.argv (command-line arguments)

# Module-level in-memory state (Session 1 only)
tasks = []  # e.g., {"id": 1, "title": "Learn Python", "completed": False}

def add_task(task_id, title):
    """Add a new task with the next available ID."""
    task = {"id": task_id, "title": title, "completed": False}
    tasks.append(task)           # mutate shared list
    print(f"Added: {title}")     # user feedback on the CLI

    print("Display tasks !!!")
    for t in tasks:
        status = "Done" if t["completed"] else "Pending"
        print(f"{t['id']}. {t['title']} - {status}")


if __name__ == "__main__":  # run only when executed directly
    """CLI parser using sys.argv (no external libs)."""
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py add [args]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py add <task_id ><task title>")
            sys.exit(1)

        task_id = sys.argv[2]
        title = " ".join(sys.argv[3:])
        add_task(task_id, title)

    else:
        print("Unknown command. Try: add")
