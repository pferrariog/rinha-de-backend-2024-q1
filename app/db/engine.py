from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///database.db")


def get_db_connection() -> Generator:
    """Instantiate a db connection"""
    with Session(engine) as session:
        yield session
