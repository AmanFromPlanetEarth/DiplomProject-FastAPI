from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///users.db"
engine = create_engine(DATABASE_URL, echo=True)
