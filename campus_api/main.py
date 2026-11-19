# pyright: reportMissingImports=false


try:
    from fastapi import FastAPI,HTTPException
    from pydantic import BaseModel
    from courses import courses
except ModuleNotFoundError:  # pragma: no cover
    class FastAPI:  # type: ignore[no-redef]
        def get(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

app = FastAPI()



 
@app.get("/")
def home():
    return {"message": "Task API is running"}

@app.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number * number}
 
@app.get("/greet1")
def greet1(name: str | None = None):
    if name is None:
        message = "Please pass in a friends name"
        raise HTTPException(status_code=400,detail=message)
    return {"message": f"Hello, {name}!"}

@app.get("/greet2")
def greet2(name: str ):
    if name is None:
        return {"message": "Hello, friend!"}
    return {"message": f"Hello, {name}!"}

@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        message = "b cannot be zero"
        raise HTTPException(status_code=400, detail=message)
    return {"result": a / b}



'''
1. Body - model class 
Model class
callng out post, they have to pass text
'''
class Note(BaseModel):
    text: str
 
notes = []
 
@app.post("/notes", status_code=201)
def add_note(note: Note):
    notes.append(note.text)
    return {"saved": note.text, "total": len(notes)}

tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": True},
    {"id": 2, "title": "Build a GET endpoint", "done": False},
    {"id": 3, "title": "Build a POST endpoint", "done": False},
]




class TaskCreate(BaseModel):
    title: str
    done: bool = False
 



@app.get("/tasks")
def list_tasks():
    return tasks
 
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# 1. model class
class TaskCreate(BaseModel):
    title: str
    done: bool = False

# 2. Post route 
@app.post("/tasks", status_code=201)
# 3, implement method, param datatype should be the name as in the model class
def create_task(task: TaskCreate):
    new_task = {"id": max(tasks) + 1,
                "title": task.title, "done": task.done}
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = task.title
            t["done"] = task.done
            return t
    message = "Task not found"
    raise HTTPException(status_code=404, detail=message)


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return
    message = "Task not found"
    raise HTTPException(status_code=404, detail=message)
