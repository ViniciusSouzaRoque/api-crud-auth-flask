from typing import List

from sqlalchemy.orm import joinedload

from persistency.connection import Session
from persistency.models.models import Tarefas, Usuarios, UsuariosTarefas
from persistency.schemas.user_schemas import UserCreateInput, UserUpdateInput
from utils.exceptions.exceptions import (
    ProjectNotFound,
    UserAlreadyExists,
    UserNotFound,
)
from utils.providers.hash_provider import generate_hash


class UserService:
    def read_user(email: str):
        with Session() as session:
            try:
                user = (
                    session.query(Usuarios)
                    .options(joinedload(Usuarios.tarefas), joinedload(Usuarios.equipes))
                    .filter_by(email=email)
                    .one()
                )
                if user:
                    return user
            except Exception:
                return None

    def list_users() -> List[Usuarios]:
        with Session() as session:
            users = (
                session.query(Usuarios)
                .options(joinedload(Usuarios.tarefas), joinedload(Usuarios.equipes))
                .all()
            )
            return users

    def associate_user_with_task(task_id: int, user_id: int):
        with Session() as session:
            tarefa = (
                session.query(Tarefas).filter_by(id=task_id).one_or_none()
            )

            if not tarefa:
                raise ProjectNotFound("Projeto não encontrado")

            user = session.query(Usuarios).filter_by(id=user_id).one_or_none()

            if not user:
                raise UserNotFound("Usuário não encontrado")

            tarefa_usuario = (
                session.query(UsuariosTarefas)
                .filter_by(tarefa_id=tarefa.id, usuario_id=user.id)
                .one_or_none()
            )

            if not tarefa_usuario:
                tarefa_usuario = UsuariosTarefas(
                    tarefa_id=tarefa.id, usuario_id=user.id
                )
                session.add(tarefa_usuario)

            session.commit()

            return True

    def disassociate_user_from_task(user_id: int, task_id: int) -> bool:
        with Session() as session:
            user = session.query(Usuarios).filter_by(id=user_id).one_or_none()
            if not user:
                raise UserNotFound("Usuário não encontrado")

            tarefa = (
                session.query(Tarefas).filter_by(id=task_id).one_or_none()
            )
            if not tarefa:
                raise ProjectNotFound("Projeto não encontrado")

            tarefa_usuario = (
                session.query(UsuariosTarefas)
                .filter_by(tarefa_id=tarefa.id, usuario_id=user.id)
                .one_or_none()
            )

            if not tarefa_usuario:
                return False

            session.delete(tarefa_usuario)
            session.commit()

        return True

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

            for project in user.projects:
                project.users.remove(user)

            session.delete(user)
            session.commit()

            return True
