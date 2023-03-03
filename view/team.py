from flask import Blueprint, request

from controller.team_services import TeamService
from utils.exceptions.exceptions import TeamAlreadyExists, TeamNotFound

team_bp = Blueprint("team", __name__)


@team_bp.route("/create/<string:name>", methods=["POST"])
@team_bp.route("/create/", methods=["POST"])
def create_team(name=None):
    try:
        if not name:
            name = request.json.get("name")

        team = TeamService.create_team(name)

    except TeamAlreadyExists:
        return {"Error": "Team Already Exists"}

    return team, 203


@team_bp.route("/update/<int:id>", methods=["PUT"])
@team_bp.route("/update/", methods=["PUT"])
def update_team(id=None):
    try:
        if not id:
            id = request.json.get("email")
        name = request.json.get("name")

        TeamService.update_team(id, name)

    except TeamNotFound:
        return {"Error": "Team Not Found"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Equipe Atualizada", 200


@team_bp.route("/delete/<int:id>", methods=["DELETE"])
@team_bp.route("/delete/", methods=["DELETE"])
def delete_team(id=None):
    try:
        if not id:
            id = request.json.get("id")
        TeamService.delete_team(id)

    except TeamNotFound:
        return {"Error": "Team not found"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Equipe Deletada", 200


@team_bp.route("/", methods=["GET"])
def list_teams():
    return {
        "teams": [team.to_dict() for team in TeamService.list_teams()]
    }, 200


@team_bp.route("/<int:id>", methods=["POST"])
@team_bp.route("/", methods=["POST"])
def read_team(id=None):
    if not id:
        id = request.json.get("id")

    team = TeamService.search_team_by_id(id)

    if not team:
        return {"Error": "Equipe não encontrada"}

    return team.to_dict(), 200
