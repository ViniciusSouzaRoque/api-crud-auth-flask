from typing import List

from persistency.connection import Session
from persistency.models.models import Tarefas
from utils.exceptions.exceptions import TaskAlreadyExists, TaskNotFound


class TaskService:
    def search_task_by_id(id: int):
        with Session() as session:
            try:
                task = session.query(Tarefas).filter_by(id=id).one()
                if task:
                    return task
            except Exception:
                return None

    def search_task_by_name(name: str):
        with Session() as session:
            try:
                task = session.query(Tarefas).filter_by(name=name).one()
                if task:
                    return task
            except Exception:
                return None

    def list_tasks() -> List[Tarefas]:
        with Session() as session:
            tasks = session.query(Tarefas).all()
            return tasks

    def create_task(name: str):
        exists = TaskService.search_task_by_name(name)

        if exists:
            raise TaskAlreadyExists("Tarefa já existente")

        with Session() as session:
            equipe = Tarefas(
                name=name,
            )
            session.add(equipe)
            session.commit()
            session.refresh(equipe)

        return {"Created": "OK!"}

    def update_task(id: int, name: str):
        with Session() as session:
            task = TaskService.search_task_by_id(id)

            if not task:
                raise TaskNotFound("Tarefa não encontrada")

            task.name = name
            session.add(task)
            session.commit()

            return task

    def delete_task(id: int):
        with Session() as session:
            task = TaskService.search_task_by_id(id)

            if not task:
                raise TaskNotFound("Tarefa não encontrada")

            session.delete(task)
            session.commit()

            return True
