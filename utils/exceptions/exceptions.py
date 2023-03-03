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
