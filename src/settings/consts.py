from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Authentication:
    USERS_CONNECTION_STRING = "postgresql+psycopg2://postgres:Pass123@localhost:5432/we-share"


