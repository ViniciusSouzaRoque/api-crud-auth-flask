from typing import List, Optional

from pydantic import BaseModel


class UserCreateInput(BaseModel):
    name: str
    email: str
    password: str
    tasks: Optional[List[int]]
    teams: Optional[List[int]]



class UserUpdateInput(BaseModel):
    name: str
    email: str


class DeleteUserInput(BaseModel):
    email: str


class UserOutput(BaseModel):
    name: str
    email: str
    tasks: Optional[List[int]]
    teams: Optional[List[int]]
