import sys

tasks = []
next_id = 1

def add_task(title):
    global next_id
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    next_id += 1
    print(f"Added: {title}")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "✅" if t["completed"] else "❌"
        print(f"{t['id']}. {t['title']} - {status}")

def mark_complete(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            print(f"Marked complete: {t['title']}")
            return
    print("Task not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py [add/list/complete] [args]")
        sys.exit(1)

    action = sys.argv[1]
    if action == "add":
        title = " ".join(sys.argv[2:])
        add_task(title)
    elif action == "list":
        list_tasks()
    elif action == "complete":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py complete <id>")
            sys.exit(1)
        mark_complete(int(sys.argv[2]))
    else:
        print("Unknown command.")
