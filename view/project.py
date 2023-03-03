from flask import Blueprint, request

from controller.project_services import ProjectService
from utils.exceptions.exceptions import ProjectAlreadyExists, ProjectNotFound

project_bp = Blueprint("project", __name__)


@project_bp.route("/create/<string:name>", methods=["POST"])
@project_bp.route("/create/", methods=["POST"])
def create_project(name=None):
    try:
        if not name:
            name = request.json.get("name")

        project = ProjectService.create_project(name)

    except ProjectAlreadyExists:
        return {"Error": "Project Already Exists"}

    return project, 203


@project_bp.route("/update/<int:id>", methods=["PUT"])
@project_bp.route("/update/", methods=["PUT"])
def update_project(id=None):
    try:
        if not id:
            id = request.json.get("email")
        name = request.json.get("name")

        ProjectService.update_project(id, name)

    except ProjectNotFound:
        return {"Error": "Project Not Found"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Equipe Atualizada", 200


@project_bp.route("/delete/<int:id>", methods=["DELETE"])
@project_bp.route("/delete/", methods=["DELETE"])
def delete_project(id=None):
    try:
        if not id:
            id = request.json.get("id")
        ProjectService.delete_project(id)

    except ProjectNotFound:
        return {"Error": "Project not found"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Equipe Deletada", 200


@project_bp.route("/", methods=["GET"])
def list_projects():
    return {
        "projects": [
            project.to_dict() for project in ProjectService.list_projects()
        ]
    }, 200


@project_bp.route("/<int:id>", methods=["POST"])
@project_bp.route("/", methods=["POST"])
def read_project(id=None):
    if not id:
        id = request.json.get("id")

    project = ProjectService.search_project_by_id(id)

    if not project:
        return {"Error": "Equipe não encontrada"}

    return project.to_dict(), 200
