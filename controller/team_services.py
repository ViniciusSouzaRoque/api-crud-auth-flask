from typing import List

from persistency.connection import Session
from persistency.models.models import Equipes
from utils.exceptions.exceptions import TeamAlreadyExists, TeamNotFound


class TeamService:
    def search_team_by_id(id: int):
        with Session() as session:
            try:
                team = session.query(Equipes).filter_by(id=id).one()
                if team:
                    return team
            except Exception:
                return None

    def search_team_by_name(name: str):
        with Session() as session:
            try:
                team = session.query(Equipes).filter_by(name=name).one()
                if team:
                    return team
            except Exception:
                return None

    def list_teams() -> List[Equipes]:
        with Session() as session:
            teams = session.query(Equipes).all()
            return teams

    def create_team(name: str):
        exists = TeamService.search_team_by_name(name)

        if exists:
            raise TeamAlreadyExists("Equipe já existente")

        with Session() as session:
            equipe = Equipes(
                name=name,
            )
            session.add(equipe)
            session.commit()
            session.refresh(equipe)

        return {"Created": "OK!"}

    def update_team(id: int, name: str):
        with Session() as session:
            team = TeamService.search_team_by_id(id)

            if not team:
                raise TeamNotFound("Equipe não encontrada")

            team.name = name
            session.add(team)
            session.commit()

            return team

    def delete_team(id: int):
        with Session() as session:
            team = TeamService.search_team_by_id(id)

            if not team:
                raise TeamNotFound("Equipe não encontrada")

            session.delete(team)
            session.commit()

            return True
