from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = Config.URL_DATABASE
Base = declarative_base()

engine = create_engine(DATABASE_URL)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def create_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    print(DATABASE_URL)
