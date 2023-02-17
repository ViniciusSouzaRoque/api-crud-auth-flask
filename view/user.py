from flask import Blueprint, request

from controller.user_services import UserService
from persistency.schemas.user_schemas import UserCreateInput

user_bp = Blueprint("user", __name__)


@user_bp.route("/create", methods=["POST"])
def create_user():
    try:
        user_input = UserCreateInput.parse_obj(request.json)
        print("Aqui foi")

    except Exception:
        return "Entrada de dados invalida", 400

    print("Passei")
    name = user_input.name
    email = user_input.email
    password = user_input.password

    user = UserService.create_user(name, email, password)

    return user
