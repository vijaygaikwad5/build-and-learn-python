## Session 4: FAST API...


## Section 1: Introduction of FastAPI
fast is async while flask is sync

- WSGI (Web Server Gateway Interface) and ASGI (Asynchronous Server Gateway Interface) are specifications defining how Python web servers and web applications communicate. The fundamental difference lies in their approach to handling requests: 

- WSGI (Synchronous):
    - Synchronous Processing: WSGI handles requests one at a time in a blocking manner. When a request comes in, the server processes it and waits for the response before moving on to the next request.
    - Concurrency: Concurrency in WSGI applications is typically achieved through multiple processes or threads, where each process/thread handles a single request.
    - Protocol Support: Primarily designed for the HTTP 1.0/1.1 request-response model. It does not natively support WebSockets or HTTP/2.
    - Use Cases: Well-suited for traditional web applications that do not require real-time features or high levels of concurrency, like many standard REST APIs or content-delivery sites.
    - Examples: Frameworks like Flask and older versions of Django primarily use WSGI. Servers include Gunicorn, uWSGI, and Apache with mod_wsgi. 
- ASGI (Asynchronous):
    - Asynchronous Processing: ASGI enables asynchronous processing, allowing applications to handle multiple requests concurrently without blocking the main thread. This is achieved using async/await keywords in Python.
    - Concurrency: ASGI is designed for efficient concurrency, making it ideal for applications with long-lived connections or those requiring high throughput and responsiveness.
    - Protocol Support: Supports a wider range of protocols, including HTTP 1.0/1.1, HTTP/2, and WebSockets, facilitating real-time and bidirectional communication.
    - Use Cases: Recommended for modern, real-time applications, such as chat applications, live dashboards, streaming services, and APIs with many concurrent clients.
    - Examples: Frameworks like FastAPI, Starlette, and newer versions of Django support ASGI. Servers include Uvicorn, Hypercorn, and Daphne.

In summary:
- WSGI is synchronous and blocking, suitable for traditional request-response applications.
- ASGI is asynchronous and non-blocking, designed for modern, real-time, and high-concurrency applications.

#### Servers: Uvicorn vs. Gunicorn
- **Uvicorn** is a fast, asynchronous server designed to implement the ASGI specification. It is used to run modern, asynchronous frameworks like FastAPI and Starlette.
- **Gunicorn** is a WSGI server used for production deployment of synchronous frameworks like Flask and Django (in its traditional WSGI mode). 
---

FastAPI uses the OpenAPI standard for defining APIs.

OpenAPI is a standardized, machine-readable format for describing REST APIs — it defines what your API does, what inputs it expects, and what responses it returns. In FastAPI, OpenAPI is used to automatically generate interactive documentation (like Swagger UI) and helps ensure consistency, validation, and easy integration across tools and teams.
learn more about OpenAPI:
- https://fastapi.tiangolo.com/tutorial/first-steps/#openapi
- https://learn.openapis.org/

let's go to fastapi official page: https://fastapi.tiangolo.com/

as you can see FastAPI is a modern, fast high-performance framework for building apis with python.
some of the key features are .... then list couple of features from the web-page ...

as we scroll further ...
as you can see fastapi has picked up a lot of sponsors and its due to fastapi getting popular day by day due to its ease of use and high performance.

---------------------------------------------------------------------------------------------------------------

## Section: Build minimal FastAPI application

lets get started with creating our FAST API application that would serve as an api endpoint for our Smart Task Tracker application.

This endpoint can be used for Integration with Dashboards or Automation tools -- FastAPI makes your task tracker usable by other systems like:

- Centralized Task Monitoring Dashboard:
lets say Program management office (PMO) team builds a dashboard that fetches tasks from 10+ teams.
each team exposes as FastAPI endpoint like /tasks from your Smart Task Tracker.
the dashboard periodically polls /tasks from every team, aggregates them and shows a central view ...

in our area lets take example of Janus - data mesh ... you can expose applications data to the data-mesh using endpoints ... data like how many instance of apps running .. number of servers, owner details... developer details ... release details like version features etc etc ...

- Chatbot Integration
let say you tell you chatbot "Mark task 2 as complete..."
The bot sends a PUT /tasks/2 call to your FastAPI.
Your app handles it silently and updates the CSV.

- Grafana Integration
Analysts fetch tasks using /tasks API endpoint and plot them in PowerBI or Grafana as "pending vs completed counts" or "Daily task completion rate"

- Integration with CI/CD pipelines
maybe you want to create a task or update a task as part of your CI/CD pipeline. like marking the task complete if the pipeline finishes successfully.

--------------------------------------------------------
let's get started with our simple minimal base FastAPI application like we did with Flask in yesterdays session ...
Let us refer FastAPI official getting started link: https://fastapi.tiangolo.com/tutorial/first-steps/

yesterday we wrote Flask application in 4 basic steps similarly we can write FastAPI application in 3 steps ...

lets get started:

lets create a file main.py:

main.py
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

As Fast api shows lets run it our app now ...

command to start the app:
```bash
fastapi dev main.py
```

ohh it complain that port 50001 is already in use ...
this happens because we are using devpod workspace and devpod has already a process running on this port ...
let's change the default port of fastapi to 5000 that where our devpod exposes service that we can access from external browser ...

updated command to start the app:
```bash
fastapi dev main.py --port 5000
```
 perfect our app starts successfully ... 
 let us access it in the browser ...
 perfect, we are getting response from our fastapi application ...

now if we access /docs route or context, we will be able to see an interactive API documentation which is provided by Swagger UI...

Oppsss /docs is not working ...
the reason for this is that Devpod attaches /proxy/5000 to the service endpoint from where we can access our application inside devpod workspace ...
had this been your local workspace /docs would have worked just fine ...
but since devpod attaches this extra context to the path ... let deal with it ...

fastapi has an option to solve this issue ...
by using option `--root-path` we can tell fastapi the starting point of our api application...

now the final command to run our fastapi will become:
```bash
fastapi dev main.py --port 5000 --root-path /proxy/5000
```
this works perfectly ... we are now able to access the /docs route...
> Note: here we are not writing our gatekeeper function in FastAPI because FastAPI itself handles it...

/docs route is an automatic interactive api documentation provided by Swagger UI...
We will be using this interactive api documentation to interact with our task tracker api application instead of curl or postman ...

For those who do not know what is Swagger UI ?
Swagger UI is an open-source tool that generates a human-friendly, web-based interface for visualizing and interacting with an API. It automatically creates interactive documentation from an OpenAPI Specification file, allowing developers, testers, and consumers to understand and test an API's endpoints without writing code

We can see in our swagger ui, we already have a GET route, let's test our api using this ...
there we go ... we got a response ...
also you can see it shows us a correspondig curl url as well that we can use on command prompt which will return the same behaviour ...

-------------------------------------------------------------------------------------------------------------------------------------

## Section 3: Understanding the code ...
now that we have our fastapi application running ... 
lets understand the code ...
Step 1: we imported FastAPI package that provides all the functionality to our API...
Step 2: we create a varialbe `app`. which is an instance of `FastAPI`. It acts as main point of interaction to create all our api endpoints just like we created routes in Flask app.
```python
app = FastAPI()
```

Step 3: creation of route...
"Route" here refers to the last part of the URL starting from the first /.

So, in a URL like:

https://example.com/api/v1/items/foo
...the route would be:

/api/v1/items/foo

> Note: A "route" is also commonly called an "endpoint" or a "path". you can use whatever suits you...

`@app` here is doing the same what it was doing in Flask -- mapping the function right below to the path/route in the case "/".
Notice we are using something called as `get` also --
what it is doing is mapping the `get` operation as well to this `/` path.
remember in flask, `GET` was the default method of operation and we didnt have to explicitly mention it ...
whereas in fastapi, for every route, you have to define the type of http method.
we have 4 types:
POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.

reference: https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function
`async` : why using the `async` keyword we are making this function run asynchronously -- so it wont block the server while its waiting for a response.
fastapi supports both `async` and `sync`

why use async becasuse this function can:
- Wait for async database queries
- Fetch data from other APIs
- Sleep or delay without blocking other users

But in our case we are not going to perform any async operations so lets just remove it ...

and then remove the `async` keyword from the program ....

Now that we have understood fastapi application and how it works ...
let's integrate it with our task_engine.py which is the brain of our program.
-------------------------------------------------------------------------------------------------------

```info
@decorator Info

That @something syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below corresponds to the path / with an operation get.

It is the "path operation decorator".
```
--------------------------------------------------------------------------------------------------

Yesterday while writing our flask app, i said we will discuss `GET` and `POST` today ...

`GET` and `POST` are http methods 

in simple words, https methods are used by clients to interact with the server
in our case ... browser is the client and our fastapi is the server ...
http method tells the server what to do with the resource(here in our case resource means the task)
like, "hey server, I want to `GET` the list of `/tasks`"
here `GET` is the http method and `/tasks` is the resource ...

When building APIs, we normally use 4 specific HTTP methods to perform a specific action.

they are:

POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.

Why Do We Have Multiple Methods?

Because not every action is the same.

You want to...	HTTP Method
Read data	GET
Create something new	POST
Update something existing	PUT
Delete something	DELETE

This separation:

Makes APIs easier to design and understand

Allows browsers and tools to optimize behavior (e.g., cache GET requests)

Improves security by limiting what types of actions are allowed


So, in OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "operations" too.






-------------------------------------------------------------------------------------------------------------------------

## Section: Integrating our core engine to fastapi ...
let's quickly do that ...

Let's start with creation of our tasks i.e. our add function ... 

first let me copy over our task_engine.py into session-4 folder and import the functions in main.py like we did for Flask application...

Now before proceeding lets understand what is a Request Body ...

In simple words, a **request body** is the data sent from the client to your API application...
like in Flask we were sending the data from client which was the browser using html form.

Similarly, **response body** is the data that your api sends to the client...

> Your API almost always has to send a **response body**. But clients don't necessarily need to send ***request bodies** all the time, sometimes they only request a path, maybe with some query parameters, but don't send a body.

In FastAPI, we will be using `Pydantic` models to define our **request bodies**

In Simple words, 
- `Pydantic` is used to define the what data is expected (in other words helps us to validate the schema of our data)...
- in our case its the `task` which is a dictionary as we discussed it in session-2.
- thus `Pydantic` helps us to **make sure that the data coming into our app is correct, complete, and clean** -- without writing a ton of manual checks to validate the incoming data...
- it automatically rejects anything that doesn't fit like,
-- missing `task_id` field, or 
-- sending task_id instead of `task_title`...
-- validating that both `task_id` and `task_title` are sent..

> Read More at: https://fastapi.tiangolo.com/tutorial/body/

Lets define our schema then...
first lets do the import BaseModel from pydantic which will help us do our data validation ...

```python
from pydantic import BaseModel
```

```python
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
```
there we go we have defined our `task` as a **python dictionary**

This says:
- Every task must have an id (as number), title (as text), and completed (true/false).
- If someone sends completed: "yes", it will throw an error — or even auto-fix it if possible.

🎯 Why it's useful:
- Saves you from writing if type(x) != int: over and over
- Validates incoming API data automatically
- Converts types safely (e.g., "false" → False)
- Catches bad inputs early, before they break your app

What is BaseModel in Pydantic?
In simple terms:
> BaseModel is the parent class provided by Pydantic that you inherit from to define structured, validated data models.
- When you create a class that extends BaseModel, you're telling Python:
> “Here’s what a valid object should look like — please check it for me.”

Now lets write our route/path for the add task operation:
```python
@app.post("/task")
def create_task(task: Task):
    task_id = task.id
    title = task.title
    add_task(task_id, title)
    return {"message": "Task added successfully"}
```

let's now write list function as well:
```python
@app.get("/tasks")
def get_tasks():
    return list_tasks()
```

lets write mark complete function:
```python
@app.put("/task/{task_id}")
def mark_complete(task_id):
    complete_task(task_id)
    return {"message": "Task marked as complete"}
```

lets now finish with delete task:
```python
@app.delete("/task/{task_id}")
def remove_task(task_id):
    delete_task(task_id)
    return {"message": "Task deleted"}
```

## Quick reference commands:
```bash
fastapi dev main.py --port 5000
```
start fastapi with a specific root directory/path
```bash
fastapi dev main.py --port 5000 --root-path /proxy/5000
```
alternatively, you can also start your fastapi with `uvicorn`
```bash
uvicorn main:app --reload --port 5000 --root-path /proxy/5000
```
