from pydantic import BaseModel


class ProjectCreateInput(BaseModel):
    name: str


class ProjectUpdateInput(BaseModel):
    name: str
