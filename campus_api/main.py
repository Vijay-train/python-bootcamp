
from typing import Annotated, Literal
from fastapi import FastAPI, HTTPException, Path, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator
import db
from psycopg.errors import UniqueViolation

app = FastAPI()


@app.get("/tasks")
def list_tasks():
    with db.get_conn() as conn:
        cur = conn.execute("SELECT * FROM tasks ORDER BY id")
        return cur.fetchall()

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    sql = "SELECT * FROM tasks WHERE id = %s"
    with db.get_conn() as conn:
        task = conn.execute(sql, (task_id,)).fetchone()
    if task is None:
        message = "Task not found"
        raise HTTPException(status_code=404, detail=message)
    return task

class TaskIn(BaseModel):
    title: str
    done: bool = False
 

@app.post("/tasks", status_code=201)
def create_task(data: TaskIn):
    sql = """INSERT INTO tasks (title, done)
             VALUES (%s, %s) RETURNING *"""
    try:
        with db.get_conn() as conn:
            cur = conn.execute(sql, (data.title, data.done))
            return cur.fetchone()
    except UniqueViolation:
        message = "That title already exists"
        raise HTTPException(status_code=409, detail=message)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, data: TaskIn):
    sql = """UPDATE tasks SET title = %s, done = %s
             WHERE id = %s RETURNING *"""
    values = (data.title, data.done, task_id)
    with db.get_conn() as conn:
        task = conn.execute(sql, values).fetchone()
    if task is None:
        message = "Task not found"
        raise HTTPException(status_code=404, detail=message)
    return task
 
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    sql = "DELETE FROM tasks WHERE id = %s RETURNING id"
    with db.get_conn() as conn:
        gone = conn.execute(sql, (task_id,)).fetchone()
    if gone is None:
        message = "Task not found"
        raise HTTPException(status_code=404, detail=message)
