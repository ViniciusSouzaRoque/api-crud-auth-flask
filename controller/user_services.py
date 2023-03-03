from typing import List

from persistency.connection import Session
from persistency.models.models import Usuarios
from persistency.schemas.user_schemas import UserCreateInput, UserUpdateInput
from utils.exceptions.exceptions import UserAlreadyExists, UserNotFound
from utils.providers.hash_provider import generate_hash


class UserService:
    def read_user(email: str):
        with Session() as session:
            try:
                user = session.query(Usuarios).filter_by(email=email).one()
                if user:
                    return user
            except Exception:
                return None

    def list_users() -> List[Usuarios]:
        with Session() as session:
            users = session.query(Usuarios).all()
            return users

    def create_user(self: UserCreateInput):
        senha_hashed = generate_hash(self.password)

        exists = UserService.read_user(self.email)

        if exists:
            raise UserAlreadyExists("Usuário existente")

        with Session() as session:
            user = Usuarios(
                name=self.name, email=self.email, password=senha_hashed
            )
            session.add(user)
            session.commit()
            session.refresh(user)

        return self

    def update_user(self: UserUpdateInput):
        with Session() as session:
            user = UserService.read_user(self.email)

            if not user:
                raise UserNotFound("Usuário não encontrado")

            user.name = self.name
            session.add(user)
            session.commit()

            return self

    def delete_user(email: str):
        with Session() as session:
            user = UserService.read_user(email)

            if not user:
                raise UserNotFound("Usuário não encontrado")

            session.delete(user)
            session.commit()

            return True
