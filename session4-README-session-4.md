# Session 4: Build a REST API for Task Tracker Using FastAPI

## Recap of Session 3

In the previous session, we took our command-line Task Tracker and built a web-based interface using Flask:
- Displayed tasks in the browser
- Added, completed, and deleted tasks using buttons and forms
- Used Jinja templates for dynamic rendering

---

## Goal of Session 4

We now move from **web UI to REST API** using **FastAPI**.

In this session, we'll:
- Install FastAPI
- Build and run our first FastAPI app (RESTful service that returns JSON)
- Understand how to validate request/response data using Pydantic models  
- Access and explore built-in Swagger UI to test API endpoints
- References:
    - https://fastapi.tiangolo.com/
    - https://fastapi.tiangolo.com/tutorial/first-steps/
---

## Workflow Overview

| Section | Topic                         | What We Will Cover                                                                 |
|---------|-------------------------------|-------------------------------------------------------------------------------------|
| 1       | Introduction to FastAPI       | What is FastAPI, benefits over Flask, real-world use cases                         |
| 2       | Project Setup                 | Installing FastAPI & Uvicorn, folder structure, running the server                 |
| 3       | Define API Endpoints          | Create `GET`, `POST`, `PUT`, `DELETE` routes for tasks                             |
| 4       | Request and Response Models   | Create structured request validation using `pydantic.BaseModel`                    |
| 5       | Implement Business Logic      | Hook up to `task_engine.py` — add, list, complete, delete                          |
| 6       | Testing the API               | How to test API endpoints using `curl`, Postman, and browser                       |
| 7       | FastAPI Swagger UI and ReDoc  | Auto docs walkthrough and debugging tips                                           |
| 8       | Bonus: Add Task Stats Endpoint| Add an endpoint to return counts of pending and completed tasks                    |

---

# Section 1: Introduction to FastAPI

What is REST API application ?
- A **REST API application** is a program that lets different systems talk to each other over the web using simple rules.
- It works like this:
    - You send a request to a specific URL (called an endpoint) using standard methods like GET, POST, PUT, or DELETE.
    - The server processes it and sends back a response — usually in JSON format.
    - Both the request and response will be in JSON format.
    - JSON looks just like a Python dictionary — something we already learned in Session 1.

In short:
> A REST API lets your app act like a service — others can call it, send it data, and get useful results back — all through clean, predictable web requests.

What is FastAPI?
- FastAPI is a python framework used to build REST API applications.
- A modern, high-performance web framework for building APIs with Python 3.6+
- Based on standard Python type hints

Why use it?
- Fast (based on Starlette and Pydantic)
- Intuitive
- Great for data validation and documentation

---

# Section 2: Project Setup

We will:
- Create a new Python file `main.py`
- Install the required packages:
  ```bash
  pip install fastapi[standard]
  ```
- Create initial folder structure:
  ```
  session4/
  ├── main.py
  ├── task_engine.py
  └── tasks.csv
  ```
- Run the FastAPI app:
  ```bash
  fastapi dev main.py --port 5000
  ```

- Test by opening: `http://localhost:5000`
- Swagger UI: `http://localhost:5000/docs`

---
# Section 3: Define API Endpoints

We will define basic endpoints:
- `GET /tasks` → List all tasks
- `POST /tasks` → Add new task
- `PUT /tasks/{id}` → Mark a task as complete
- `DELETE /tasks/{id}` → Delete a task

Use Python decorators like `@app.get()`, `@app.post()` to map URLs to functions.

We’ll demonstrate sending and receiving JSON using request bodies and path parameters.

---

# Section 4: Request and Response Models

What is a Pydantic model?
- A way to define data structure using Python classes
- Used by FastAPI for validating request payloads

Example:
```python
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
```

We’ll use these models to:
- Accept structured input
- Return consistent output
- Ensure type safety and data validation

---


# Section 5: Implement API Logic

Reuse `task_engine.py` from Sessions 2 and 3.

For each route:
- Call functions like `list_tasks()`, `add_task()`, etc.

Example:
```python
@app.get("/tasks")
def get_tasks():
    return list_tasks()
```

---


# Section 6: Testing the API

We will now test each route using the **interactive Swagger UI** that comes built into FastAPI.

FastAPI automatically provides a web-based interface at the `/docs` path where you can:
- View all available endpoints (`GET`, `POST`, `PUT`, `DELETE`)
- Try them out directly from your browser
- Provide JSON request bodies for POST or PUT requests
- Instantly see the response, status code, and returned data

### Steps:
1. Open the browser and go to:
http://localhost:5000/docs
> Note: if you are using Devpod, then open the browser using my-service dropdown.
2. Click on the endpoint you want to test (for example, `/tasks` or `/task/{task_id}`).
3. Click **“Try it out”**.
4. Enter the required parameters or request body.
5. Click **“Execute”** to send the request.
6. See the live response below the “Responses” section — it shows both:
- The JSON output
- The status code (e.g., 200 OK, 201 Created)

This built-in Swagger UI replaces the need for using external tools like curl or Postman — everything can be tested interactively within your browser.


---


# Section 7: FastAPI Swagger

FastAPI auto-generates documentation:
- Swagger UI → `http://localhost:5000/docs`

This help you:
- Test endpoints without Postman
- Share API spec with frontend teams
- Debug input/output structures

You’ll also see:
- Supported HTTP methods
- Sample request payloads
- Model schemas

---

# Section 8: Bonus Challenge – Task Stats Endpoint

Build a new endpoint:
```python
@app.get("/stats")
def get_stats():
    return {"total": 10, "completed": 6, "pending": 4}
```

This will teach:
- Custom logic in API views
- Filtering and counting tasks from CSV
- Returning computed results as JSON
