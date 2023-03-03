from .base import BaseInternalException


class UserAlreadyExists(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="Error inserting on database",
            description=description,
            status_code=400,
        )


class UserNotFound(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="User not found",
            description=description,
            status_code=400,
        )


class TeamAlreadyExists(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="Error inserting on database",
            description=description,
            status_code=400,
        )


class TeamNotFound(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="Team not found",
            description=description,
            status_code=400,
        )


class ProjectAlreadyExists(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="Error inserting on database",
            description=description,
            status_code=400,
        )


class ProjectNotFound(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="Project not found",
            description=description,
            status_code=400,
        )


class TaskAlreadyExists(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="Error inserting on database",
            description=description,
            status_code=400,
        )


class TaskNotFound(BaseInternalException):
    def __init__(self, description: str):
        super().__init__(
            name="Task not found",
            description=description,
            status_code=400,
        )
