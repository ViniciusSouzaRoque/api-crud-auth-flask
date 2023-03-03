from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = Config.URL_DATABASE
Base = declarative_base()

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)


def create_db():
    Base.metadata.create_all(bind=engine)
