
# Session 4: FAST API...

## Section 1: Introduction of FastAPI
Give history of fastapi, why it is used ... what is asyn framework ... difference between fastapi and flask ... fast is async while flask is sync

FastAPI uses the OpenAPI standard for defining APIs.

OpenAPI is a standardized, machine-readable format for describing REST APIs — it defines what your API does, what inputs it expects, and what responses it returns. In FastAPI, OpenAPI is used to automatically generate interactive documentation (like Swagger UI) and helps ensure consistency, validation, and easy integration across tools and teams.

Learn more about OpenAPI:
- https://fastapi.tiangolo.com/tutorial/first-steps/#openapi
- https://learn.openapis.org/

Let's go to the FastAPI official page: https://fastapi.tiangolo.com/

As you can see FastAPI is a modern, fast high-performance framework for building APIs with Python.  
Some of the key features are ... (then list couple of features from the web-page)

As we scroll further ...  
As you can see FastAPI has picked up a lot of sponsors and it's due to FastAPI getting popular day by day due to its ease of use and high performance.

## Section 2: Build minimal FastAPI application
Let’s get started with creating our FAST API application that would serve as an API endpoint for our Smart Task Tracker application.

This endpoint can be used for integration with Dashboards or Automation tools — FastAPI makes your task tracker usable by other systems like:

### Centralized Task Monitoring Dashboard:
Let’s say Program Management Office (PMO) team builds a dashboard that fetches tasks from 10+ teams.  
Each team exposes a FastAPI endpoint like `/tasks` from your Smart Task Tracker.  
The dashboard periodically polls `/tasks` from every team, aggregates them and shows a central view.

In our area let’s take example of **Janus - Data Mesh**...  
You can expose applications data to the data-mesh using endpoints...  
Data like how many instance of apps running, number of servers, owner details, developer details, release details like version, features etc etc ...

### Chatbot Integration:
Let’s say you tell your chatbot:  
**"Mark task 2 as complete"**  
The bot sends a `PUT /tasks/2` call to your FastAPI.  
Your app handles it silently and updates the CSV.

### Grafana Integration:
Analysts fetch tasks using `/tasks` API endpoint and plot them in PowerBI or Grafana as "pending vs completed counts" or "daily task completion rate".

### CI/CD Integration:
Maybe you want to create a task or update a task as part of your CI/CD pipeline — like marking the task complete if the pipeline finishes successfully.

Let’s get started with our simple minimal base FastAPI application like we did with Flask in yesterday’s session...

Let us refer FastAPI official getting started link: https://fastapi.tiangolo.com/tutorial/first-steps/

Yesterday we wrote Flask application in 4 basic steps.  
Similarly, we can write FastAPI application in 3 steps.

Let’s get started:

Create a file `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### Command to start the app:
```bash
fastapi dev main.py
```

Ohh it complains that port 50001 is already in use...  
This happens because we are using devpod workspace and devpod already has a process running on this port...

Let’s change the default port of FastAPI to `5000` — that’s where our devpod exposes service that we can access from external browser...

### Updated command:
```bash
fastapi dev main.py --port 5000
```

Perfect, our app starts successfully!  
Let us access it in the browser...  
Perfect, we are getting a response from our FastAPI application...

Now if we access `/docs` path, we’ll see interactive API docs powered by Swagger UI.

Oops — `/docs` is not working...

**Why?**  
Devpod attaches `/proxy/5000` to the service endpoint.  
Had this been your local workspace, `/docs` would’ve worked fine...

To fix this, FastAPI provides an option:  
Use `--root-path` to set the app’s true base URL.

### Final command:
```bash
fastapi dev main.py --port 5000 --root-path /proxy/5000
```

Now `/docs` works perfectly! ✅

> Note: here we are **not writing our gatekeeper function** in FastAPI because FastAPI itself handles it.

## About Swagger UI
`/docs` route is an automatic interactive API documentation powered by **Swagger UI**.

We will be using this instead of curl/Postman.

### What is Swagger UI?
Swagger UI is an open-source tool that generates a human-friendly, web-based interface for visualizing and interacting with an API.  
It automatically creates interactive docs from OpenAPI specs — letting devs understand and test APIs easily.

## Section 3: Understanding the Code
Let’s understand the basic code:

### Step 1:
We imported `FastAPI` package

### Step 2:
We create an instance of FastAPI:
```python
app = FastAPI()
```

This is like the "main object" that handles all routing, responses, etc.

### Step 3:
Creation of route: A route is the path (like `/`) mapped to a function.

Example:
```python
@app.get("/")
def root():
    return {"message": "Hello"}
```

> `@app.get("/")` maps the function to a `GET` request at `/`

In Flask, `GET` is the default.  
In FastAPI, you must explicitly declare `@app.get()`, `@app.post()`, etc.

### Supported HTTP Methods:
- `GET`: Read data
- `POST`: Create data
- `PUT`: Update data
- `DELETE`: Delete data

### What is `async`?
Adding `async def` tells FastAPI the function is non-blocking and can handle multiple requests better.

But we’re not using async features here — so we can skip it.

## Decorator Info
A `@decorator` in Python is a special syntax that wraps a function with extra behavior.

> In FastAPI, `@app.get("/tasks")` tells FastAPI: “The function below is for handling GET requests to /tasks.”

## Section 4: Integrating Core Engine with FastAPI
Let’s copy over `task_engine.py` and import its functions into `main.py`.

### What is a Request Body?
- A **request body** is the data sent by the client (e.g., form data, JSON)
- A **response body** is the data your API sends back

To validate incoming data, we use `Pydantic`.

### Pydantic Model
```python
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
```

This ensures:
- `id` must be an integer
- `title` must be a string
- `completed` is a boolean (default `False`)

### Add Task Route
```python
@app.post("/task")
def create_task(task: Task):
    task_id = task.id
    title = task.title
    add_task(task_id, title)
    return {"message": "Task added successfully"}
```

### List Tasks Route
```python
@app.get("/tasks")
def get_tasks():
    return list_tasks()
```

### Complete Task Route
```python
@app.put("/task/{task_id}")
def mark_complete(task_id):
    complete_task(task_id)
    return {"message": "Task marked as complete"}
```

### Delete Task Route
```python
@app.delete("/task/{task_id}")
def remove_task(task_id):
    delete_task(task_id)
    return {"message": "Task deleted"}
```

## Quick Reference Commands
```bash
fastapi dev main.py --port 5000
```

With proxy path for Devpod:
```bash
fastapi dev main.py --port 5000 --root-path /proxy/5000
```

Or using Uvicorn:
```bash
uvicorn main:app --reload --port 5000 --root-path /proxy/5000
```
