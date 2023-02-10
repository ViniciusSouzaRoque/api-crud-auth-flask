from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import Config

DATABASE_URL = Config.DATABASE_URL
SCHEMA = "backend"
Base = declarative_base()


engine = create_engine(DATABASE_URL)
session = sessionmaker(
    bind=engine, autocommit=False, autoflush=False
)

def create_db(schema=SCHEMA):
    Base.metadata.create_all(bind=engine, schema=schema)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
