from pydantic import BaseModel, StringConstraints
from typing import Annotated

class TaskCreate(BaseModel):
    title: Annotated[
        str,
        StringConstraints(min_length=1, max_length=100)
    ]

class TaskUpdate(BaseModel):
    done: bool