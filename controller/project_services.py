from typing import List

from persistency.connection import Session
from persistency.models.models import Projetos
from utils.exceptions.exceptions import ProjectAlreadyExists, ProjectNotFound


class ProjectService:
    def search_project_by_id(id: int):
        with Session() as session:
            try:
                project = session.query(Projetos).filter_by(id=id).one()
                if project:
                    return project
            except Exception:
                return None

    def search_project_by_name(name: str):
        with Session() as session:
            try:
                project = session.query(Projetos).filter_by(name=name).one()
                if project:
                    return project
            except Exception:
                return None

    def list_projects() -> List[Projetos]:
        with Session() as session:
            projects = session.query(Projetos).all()
            return projects

    def create_project(name: str):
        exists = ProjectService.search_project_by_name(name)

        if exists:
            raise ProjectAlreadyExists("Equipe já existente")

        with Session() as session:
            equipe = Projetos(
                name=name,
            )
            session.add(equipe)
            session.commit()
            session.refresh(equipe)

        return {"Created": "OK!"}

    def update_project(id: int, name: str):
        with Session() as session:
            project = ProjectService.search_project_by_id(id)

            if not project:
                raise ProjectNotFound("Equipe não encontrada")

            project.name = name
            session.add(project)
            session.commit()

            return project

    def delete_project(id: int):
        with Session() as session:
            project = ProjectService.search_project_by_id(id)

            if not project:
                raise ProjectNotFound("Equipe não encontrada")

            session.delete(project)
            session.commit()

            return True
