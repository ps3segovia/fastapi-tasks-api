from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Tasks API",
    description="A simple API to manage tasks.",
    version="0.1.0"
)

app.include_router(router)