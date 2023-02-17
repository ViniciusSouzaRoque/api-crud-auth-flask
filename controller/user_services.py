from persistency.connection import Session
from persistency.models.models import Usuarios
from utils.providers.hash_provider import generate_hash


class UserService:
    def create_user(name: str, email: str, senha: str):
        senha_hashed = generate_hash(senha)

        with Session() as session:
            user = Usuarios(name=name, email=email, password=senha_hashed)
            session.add(user)
            session.commit()
            session.refresh(user)

        return {"name": name, "email": email}
