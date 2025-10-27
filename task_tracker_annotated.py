
# task_tracker_annotated.py
# ---------------------------------------------
# Session 1 — Smart Task Tracker (Annotated)
# Identical behavior to task_tracker.py, with line-by-line explanations.
# Status legend: [Done] / [Pending]

import sys  # for sys.argv (command-line arguments)

# Module-level in-memory state (Session 1 only)
tasks = []      # e.g., {"id": 1, "title": "Learn Python", "completed": False}
next_id = 1     # auto-incrementing identifier

def add_task(title: str) -> None:
    """Add a new task with the next available ID."""
    global next_id  # we reassign next_id, so declare it global
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)          # mutate shared list
    next_id += 1                # prepare for the next insertion
    print(f"Added: {title}")    # user feedback on the CLI

def list_tasks() -> None:
    """Print all tasks and their status."""
    if not tasks:               # empty list => falsy
        print("No tasks yet.")
        return
    for t in tasks:
        status = "[Done]" if t["completed"] else "[Pending]"
        print(f"{t['id']}. {t['title']} - {status}")

def mark_complete(task_id: int) -> None:
    """Mark the task with given id as completed, if it exists."""
    for t in tasks:             # linear scan (fine for small lists)
        if t["id"] == task_id:
            t["completed"] = True
            print(f"Task {task_id} marked complete!")
            return             # stop after first match
    print("Task not found.")    # graceful fallback

if __name__ == "__main__":      # run only when executed directly
    """CLI parser using sys.argv (no external libs)."""
    if len(sys.argv) < 2:
        print("Usage: python task_tracker_annotated.py [add|list|complete] [args]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker_annotated.py add <task title>")
            sys.exit(1)
        title = " ".join(sys.argv[2:])  # rebuild multi-word input
        add_task(title)

    elif action == "list":
        list_tasks()

    elif action == "complete":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker_annotated.py complete <id>")
            sys.exit(1)
        mark_complete(int(sys.argv[2]))  # cast to int (ValueError on bad input)

    else:
        print("Unknown command. Try: add, list, or complete.")

