from pydantic import BaseModel


class TaskCreateInput(BaseModel):
    name: str


class TaskUpdateInput(BaseModel):
    name: str
