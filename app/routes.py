from fastapi import  APIRouter, HTTPException
from typing import Annotated
from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated


router = APIRouter()

# Временное хранилище задач (в памяти)
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a pet project", "done": False},
]

class TaskCreate(BaseModel):
    title: Annotated[
        str,
        StringConstraints(min_length=1, max_length=100)
    ]

class TaskUpdate(BaseModel):
    done: bool

@router.get('/')
def read_root():
    return {"message": "Welcome to Tasks API!"}

@router.get("/hello/{name}")
def say_hello(name: Annotated[str, StringConstraints(min_length=2, max_length=20)]):
    return {"message:": f"hello {name}!"}

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: TaskCreate):
    # Генерируем новый ID (простой способ — взять макс ID + 1)
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    
    # Создаём новую задачу
    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }
    
    # Сохраняем в памяти
    tasks.append(new_task)
    
    return new_task

@router.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = task_update.done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

