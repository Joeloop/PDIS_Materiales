from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection = f"sqlite:///../Database/database.db"
engine = create_engine(connection)
Base = declarative_base()
