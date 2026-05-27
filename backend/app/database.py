from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool

from app.config import get_settings

settings = get_settings()

# Use connect_args for SQLite compatibility if testing locally;
# for PostgreSQL this is ignored.
engine = create_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
