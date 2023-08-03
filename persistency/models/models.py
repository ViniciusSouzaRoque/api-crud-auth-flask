from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from persistency.connection import Base


class Usuarios(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=50), nullable=False)
    email = Column(String(length=50), nullable=False, unique=True)
    password = Column(String(length=100), nullable=False)

    tarefas = relationship(
        "Tarefas", secondary="usuarios_tarefas", back_populates="usuarios"
    )

    equipes = relationship(
        "Equipes", secondary="usuarios_equipes", back_populates="usuarios"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "tasks": [t.to_dict() for t in self.tarefas],
            "equipes": [e.to_dict() for e in self.equipes],
        }


class Tarefas(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=50), nullable=False)

    usuarios = relationship(
        "Usuarios", secondary="usuarios_tarefas", back_populates="tarefas"
    )

    equipes = relationship(
        "Equipes", secondary="equipes_tarefas", back_populates="tarefas"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Equipes(Base):
    __tablename__ = "equipes"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=50), nullable=False)

    tarefas = relationship(
        "Tarefas", secondary="equipes_tarefas", back_populates="equipes"
    )

    usuarios = relationship(
        "Usuarios", secondary="usuarios_equipes", back_populates="equipes"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class UsuariosEquipes(Base):
    __tablename__ = "usuarios_equipes"
    usuario_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    equipe_id = Column(Integer, ForeignKey("equipes.id"), primary_key=True)


class UsuariosTarefas(Base):
    __tablename__ = "usuarios_tarefas"
    usuario_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    tarefa_id = Column(Integer, ForeignKey("tarefas.id"), primary_key=True)


class EquipesTarefas(Base):
    __tablename__ = "equipes_tarefas"
    equipe_id = Column(Integer, ForeignKey("equipes.id"), primary_key=True)
    tarefa_id = Column(Integer, ForeignKey("tarefas.id"), primary_key=True)
