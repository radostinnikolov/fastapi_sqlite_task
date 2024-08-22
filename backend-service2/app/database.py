from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_PATH = "sqlite:///db/db_service2.db"

ENGINE = create_engine(DB_PATH, connect_args={
    "check_same_thread": False
})

SESSION = sessionmaker(bind=ENGINE, autoflush=False, autocommit=False)
BASE = declarative_base()


def access_db():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()
