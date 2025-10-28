# 🧑‍🏫 Trainer Script – Session 2: CSV Storage & Basic Task Operations

## Intro:
"Good Morning everyone, welcome back!

In our last session, we laid the foundation for our Smart Task Tracker application. 

We wrote our very first function `add_task`.

with help of which we were able to  add a task from the command line using a Python script. 

Along the way, we also learned the core concepts like variables, strings, lists, dictionaries, CLI arguments, and how to run and structure basic Python programs.

Now here’s the thing — our app could take a task, but it didn’t remember anything. The moment python script exited, everything was gone.

So in this session, we’re going to teach our app how to remember our tasks.

We’ll learn about file handling using CSV files and store our tasks to a csv file...

By the end of session, we’ll be able to:

- Store our tasks in a CSV file

- Load and display tasks

- Mark tasks as complete

- Delete tasks if needed

And all of this will happen through Python functions that we will be building in this session —  real code solving real problems."

---

## Section 1: What is a CSV File?

So before we dive into code, let’s talk about **CSV files**.

CSV stands for **Comma-Separated Values** — think of it like a super simple Excel sheet in a text file. Each line is a row, and values are separated by commas.

Example:
```
id,title,completed
1,Learn Python,False
2,Build a tracker,True
```

if we look closely at the data, each row has comma separated values...
sounds familiar... we saw in session 1 yesterday ...
a list is collection of elements/value separated by comma.
thus we can treat each row as list...

and then if we map each row to the header then we get key-value pairs ...
and that's what a dictionary is ..  a key-value pair that we learnt yesterday...

this is why yesterday's session was important for us to understand the basics of lists and dictionaries...

We’ll use this format to **store our task data** so it doesn’t disappear every time we close the program.

---

## Section 2: Add Task — Simplified

“Let’s pick up from Session 1.

First we will be simplifying our `add_task()` function — no more `global task_id`.  
We’ll take `task_id` directly from the system arguments.
```python
def add_task(task_id, title):
    """Add a new task with the next available ID."""
    task = {"id": task_id, "title": title, "completed": False}
    tasks.append(task)           # mutate shared list
    print(f"Added: {title}")     # user feedback on the CLI

    print("Display tasks !!!")
    for t in tasks:
        status = "Done" if t["completed"] else "Pending"
        print(f"{t['id']}. {t['title']} - {status}")
```

Update the main gatekeeper as well...
```python
    task_id = sys.argv[2]
    title = " ".join(sys.argv[3:])
    add_task(task_id, title)
```
The command format becomes:
```
python task_tracker.py add 1 "Learn Python"
```
---
## Section 3: Upgrade `add_task()` function from saving task to list to an actual csv file

```python
def add_task(task_id, title):
    """Add a new task with the given ID and title."""
    ensure_csv_exists()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        task = {"id": task_id, "title": title, "completed": "False"}
        writer.writerow(task)
    print(f"Task added: {title}")
```

let us create a csv file using `with` command.
```python
with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
```
Let’s understand what is happening here...

🧠 Trainer tip:
> “The `with` statement is like saying: ‘Open this file, and when I’m done, close it automatically — even if something goes wrong.’  
It helps keeps your code clean and avoid any issues from open files.”
#### (so if you're not using `with`, you should close it manually)

`open()` is a python function that returns a file object which is used to connect to a file to read, write or append it ... 

#### `open(CSV_FILE, "w", newline="", encoding="utf-8")`

- `"w"` means **write mode** – it **creates/truncates** the file.
- `"a"` means **append mode** – adds content/rows to the file without deleting existing content. creates the file if it does not exist.
- `"r"` means **read mode** - is for reading the file only

#### Why `newline=""`?

Prevents Python from adding **extra blank lines** between rows in Windows.
Always use `newline=""` when writing CSV files.

#### Why `encoding="utf-8"`?

- Ensures the file can store **international characters** like emojis, accents, etc.
- UTF-8 is the **most universal and portable** encoding.
- Ensures compatibility across platforms.

#### what is `f` ?
This is just naming. You can call it anything — as file, as file_handle, etc. But f as short is bring used traditionally.
It refers to the file object that’s returned by the open() function.
> DO NOT MENTION THIS Its data type is <class '_io.TextIOWrapper'>.

So what is a TextIOWrapper?
It’s Python’s built-in way of wrapping around a file on disk and giving you methods to read, write, or append text.
Think of f as the remote control you use to interact with the file.
Examples of what you can do with f:
> f.write("Hello World")
> f.read()
>f.close()  


3. Next, we create a **DictWriter**:
```python
writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
```
### csv.DictWriter

Writes dictionaries as rows in a CSV file. it takes 2 parameters.
1. the file object -- we already know that we created it in with statement.
2. fieldnames

#### lets understand what are `fieldnames` ?

It defines the column headers that will be used in your CSV file. Every row written using `writer.writerow()` or `writer.writerows()` must match these field names.

#### What is `FIELDNAMES`?

`FIELDNAMES` is just a variable — a list of strings that represent your column names. let us define it ...

```python
FIELDNAMES = ["id", "title", "completed"]
```

By convention, it's written in **all uppercase** to indicate it's a constant (a value that shouldn't change throughout the program).

#### Why it's important

If the keys in your dictionary don’t match the names in `fieldnames`, you'll get a `ValueError`. That’s why it's good practice to define `FIELDNAMES` once and reuse it.

#### What happens behind the scenes?

- The first row in our CSV will be: `id,title,completed`
- Every dictionary we write should have keys `"id"`, `"title"`, and `"completed"`

#### Official Python Docs

For more information:  
[https://docs.python.org/3/library/csv.html#csv.DictWriter](https://docs.python.org/3/



---

```python
writer = csv.DictWriter(f, fieldnames=["id", "title", "completed"])
writer.writeheader()
writer.writerow({"id": 1, "title": "Learn Python", "completed": "False"})


def add_task(task_id, title):
    """Add a new task with the given ID and title."""
    ensure_csv_exists()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        task = {"id": task_id, "title": title, "completed": "False"}
        writer.writerow(task)
    print(f"Task added: {title}")

```

- `writer` is an instance of `csv.DictWriter`
- `fieldnames` defines the CSV columns
- Use `writeheader()` to write the header row
- Use `writerow()` to write one row
- Use `writerows()` to write multiple rows

### DictWriter.writeheader()

Writes a single header row to the CSV file.

```python
writer.writeheader()
```

### DictWriter.writerows()

Writes multiple rows (list of dictionaries) in one call.

```python
rows = [{"id": 1, "title": "X", "completed": "False"}, {...}]
writer.writerows(rows)
```
### Common Terms

- `reader`, `writer`: These are just variable names. They hold the DictReader/DictWriter objects.
- `fieldnames`: Must match the keys of the dictionaries you write.
- Data is always string-based in CSV unless explicitly parsed.


4. Our task dictionary:
```python
task = {"id": task_id, "title": title, "completed": "False"}
```
Call back to Session 1 — remember how we used a dictionary? Same idea.

5. Finally, write the row:
```python
writer.writerow(task)
```

✅ Run the command a few times.
```
python task_tracker.py add 1 "Learn Python"
```

Then open the file — see the data added.

> We are now successfully able to store data i.e. our task in a csv file...

> Let us further enhance our application by creating a function that will first do a check if our csv file exists and if it does not then it will create it with required headers...

>> NOTE: remove the write.headers like from `add_task` and move it to `ensure_csv_exists()`

## Section 4: Check if CSV File Exists

“Let’s write a function called `ensure_csv_exists()`.

It checks if `tasks.csv` exists.

If yes, we do nothing. If not, we create it with a proper header row.

```python
def ensure_csv_exists():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
```
> add this function to the begining of `add_task()` ... 
this is how your final `add_task()` function looks like..
```python
def add_task(task_id, title):
    """Add a new task with the given ID and title."""
    ensure_csv_exists()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        task = {"id": task_id, "title": title, "completed": "False"}
        writer.writerow(task)
    print(f"Task added: {title}")
    list_tasks()
```
---

## Section 5: List All Tasks

Let’s show all the saved tasks.

We’ll use this snippet:

```python
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["completed"] == "True":
            status = "Done"
        else:
            status = "Pending"
        print(f"{row['id']}. {row['title']} — {status}")
```

🧠 Explain line-by-line:
- `DictReader` lets us access each row like a dictionary
- We check if completed is True, then show status accordingly
- Then we print it like a mini report


### csv.DictReader

Reads a CSV file row by row and maps each row to a dictionary using the headers.

The `csv.DictReader` in Python **requires headers** in the first row of the CSV file. These headers define the keys for each dictionary it reads.

If headers like `id,title,completed` are missing:
- `DictReader` will treat the first **data row** as headers.
- You’ll get incorrect keys like `'1'`, `'Learn Python'`, which break your logic.
- Accessing `row["title"]` will throw a `KeyError`.

Always write headers once when creating the file, using:
```python
writer.writeheader()
```
This keeps your file readable and compatible with future reads.

```python
reader = csv.DictReader(f)
for row in reader:
    print(row["title"])
```

- `reader` is an instance of `csv.DictReader`
- It uses the **first row** in the file as keys (column names)
- Each row is returned as a dictionary



Try running:
```
python task_tracker.py list
```

---

## Section 6: Mark a Task Complete

> Now that we have learned about reader and writer ...
> let us combine them and use to create our next function to mark a task as complete.

We’ll now write `complete_task(task_id)`.

Steps:
- Read all rows from CSV
- If ID matches, update `completed` to `"True"`
- Write all rows back

Talk through the logic:
- Use a loop to go row by row
- Store rows in a new list
- Write the updated list back

Use the same tools — `DictReader`, `DictWriter`, `writeheader`, `writerows`

Command to try:
```
python task_tracker.py complete 2
```

Check if status updates to Done.

---

## Section 7: Delete a Task

Almost same logic as complete:

- Read all rows
- Skip the one matching the given ID
- Write others back

Call it with:
```
python task_tracker.py delete 2
```

Boom — task deleted.

Wrap the session with:
> “Now your task app has storage, display, update, and delete — all powered by Python and a humble CSV file.”
