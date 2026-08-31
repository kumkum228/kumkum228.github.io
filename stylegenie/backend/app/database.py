"""
database.py
-----------
Sets up the connection to MySQL using SQLAlchemy.

- `engine`      : the low-level connection to the database.
- `SessionLocal`: a factory that creates a new DB session per request.
- `Base`        : the parent class every table model will inherit from.
- `get_db()`    : a FastAPI dependency that hands a session to a route and
                  makes sure it is always closed afterwards.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

# echo=False keeps the console quiet; set to True to see every SQL statement.
# pool_pre_ping avoids "MySQL has gone away" errors after idle time.
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Yield a database session and always close it when the request ends."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
