from sqlalchemy import Column, Integer, String

from persistency.connection import Base


class Usuarios(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=50), nullable=False)
    email = Column(String(length=50), nullable=False, unique=True)
    password = Column(String(length=100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }


class Projetos(Base):
    __tablename__ = "projetos"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=50), nullable=False)


class Tarefas(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=50), nullable=False)


class Equipes(Base):
    __tablename__ = "equipes"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=50), nullable=False)
