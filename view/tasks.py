from flask import Blueprint, request

from controller.task_services import TaskService
from utils.exceptions.exceptions import TaskAlreadyExists, TaskNotFound

task_bp = Blueprint("task", __name__)


@task_bp.route("/create/<string:name>", methods=["POST"])
@task_bp.route("/create/", methods=["POST"])
def create_task(name=None):
    try:
        if not name:
            name = request.json.get("name")

        task = TaskService.create_task(name)

    except TaskAlreadyExists:
        return {"Error": "Task Already Exists"}

    return task, 203


@task_bp.route("/update/<int:id>", methods=["PUT"])
@task_bp.route("/update/", methods=["PUT"])
def update_task(id=None):
    try:
        if not id:
            id = request.json.get("email")
        name = request.json.get("name")

        TaskService.update_task(id, name)

    except TaskNotFound:
        return {"Error": "Task Not Found"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Equipe Atualizada", 200


@task_bp.route("/delete/<int:id>", methods=["DELETE"])
@task_bp.route("/delete/", methods=["DELETE"])
def delete_task(id=None):
    try:
        if not id:
            id = request.json.get("id")
        TaskService.delete_task(id)

    except TaskNotFound:
        return {"Error": "Task not found"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Equipe Deletada", 200


@task_bp.route("/", methods=["GET"])
def list_tasks():
    return {
        "tasks": [task.to_dict() for task in TaskService.list_tasks()]
    }, 200


@task_bp.route("/<int:id>", methods=["POST"])
@task_bp.route("/", methods=["POST"])
def read_task(id=None):
    if not id:
        id = request.json.get("id")

    task = TaskService.search_task_by_id(id)

    if not task:
        return {"Error": "Equipe não encontrada"}

    return task.to_dict(), 200
