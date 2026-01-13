from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

# Создаём таблицы при запуске (если их нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tasks API",
    description="A simple API for managing tasks",
    version="0.1.0"
)

app.include_router(router)