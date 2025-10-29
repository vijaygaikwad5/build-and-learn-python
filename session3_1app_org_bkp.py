from flask import Flask, render_template, request, redirect
from task_engine import add_task, list_tasks, complete_task, delete_task

app = Flask(__name__)

@app.route("/")
def index():
    tasks = list_tasks()
    return render_template("index.html", tasks=tasks)

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
    app.run(debug=True)
