from pydantic import BaseModel


class UserCreateInput(BaseModel):
    name: str
    email: str
    password: str


class UserUpdateInput(BaseModel):
    name: str
    email: str


class DeleteUserInput(BaseModel):
    email: str


class UserOutput(BaseModel):
    name: str
    email: str
