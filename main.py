from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated

class TaskCreate(BaseModel):
    title: Annotated[
        str,
        StringConstraints(min_length=1, max_length=100)
    ]

app = FastAPI()

# Временное хранилище задач (в памяти)
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a pet project", "done": True},
]

@app.get('/')
def read_root():
    return {"message": "Welcome to Tasks API!"}

@app.get("/hello/{name}")
def say_hello(name: Annotated[str, StringConstraints(min_length=2, max_length=20)]):
    return {"message:": f"hello {name}!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
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