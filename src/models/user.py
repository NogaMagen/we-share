from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
