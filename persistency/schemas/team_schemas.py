from pydantic import BaseModel


class TeamCreateInput(BaseModel):
    name: str


class TeamUpdateInput(BaseModel):
    name: str


class DeleteUserInput(BaseModel):
    email: str


class UserOutput(BaseModel):
    name: str
    email: str
