from sqlalchemy import Column, Integer, String

from persistency.connection import Base

class Usuarios(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)


class Projetos(Base):
    __tablename__ = "projetos"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)


class Tarefas(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)

class Equipes(Base):
    __tablename__ = "equipes"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)