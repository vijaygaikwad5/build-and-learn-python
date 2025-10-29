from flask import Flask, render_template, redirect, request
from task_engine import list_tasks, add_task, delete_task, complete_task

app = Flask(__name__)

@app.route("/")
def home():
    tasks = list_tasks()
    return render_template("home.html", tasks=tasks)

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}"

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task_id = request.form.get("id")
        title = request.form.get("title")
        if task_id and title:
            add_task(task_id, title)
        return redirect("/")
    return render_template("add.html")

@app.route("/complete/<task_id>")
def complete(task_id):
    complete_task(task_id)
    return redirect("/")

@app.route("/delete/<task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)