from flask import Blueprint, request

from controller.user_services import UserService
from persistency.schemas.user_schemas import UserCreateInput, UserUpdateInput
from utils.exceptions.exceptions import UserAlreadyExists, UserNotFound

user_bp = Blueprint("user", __name__)


@user_bp.route("/create", methods=["POST"])
def create_user():
    try:
        user_input = UserCreateInput.parse_obj(request.json)
        user = UserService.create_user(user_input)

    except UserAlreadyExists:
        return {"Error": "User Already Exists"}

    return user.__dict__, 201


@user_bp.route("/update/<string:email>", methods=["PUT"])
@user_bp.route("/update/", methods=["PUT"])
def update_user(email=None):
    try:
        if not email:
            email = request.json.get("email")
        user_input = UserUpdateInput.parse_obj(request.json)
        user_input.email = email
        UserService.update_user(user_input)

    except UserNotFound:
        return {"Error": "Error"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Usuário Atualizado", 200


@user_bp.route("/delete/<string:email>", methods=["DELETE"])
@user_bp.route("/delete/", methods=["DELETE"])
def delete_user(email=None):
    try:
        if not email:
            email = request.json.get("email")
        UserService.delete_user(email)

    except UserNotFound:
        return {"Error": "User not found"}, 404

    except Exception:
        return {"Error": "Error"}, 404

    return "Usuário Deletado", 200


@user_bp.route("/", methods=["GET"])
def list_users():
    return {
        "users": [user.to_dict() for user in UserService.list_users()]
    }, 200


@user_bp.route("/<string:email>", methods=["POST"])
@user_bp.route("/", methods=["POST"])
def read_user(email=None):
    user = None
    if email:
        user = UserService.read_user(email)

    else:
        email = request.json.get("email")
        user = UserService.read_user(email)

    if not user:
        return {"Error": "Usuário não encontrado"}

    return user.to_dict(), 200
