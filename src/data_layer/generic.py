from sqlalchemy import create_engine, Engine, Select, Insert
from sqlalchemy.orm import Session


class SqlDBDataLayer:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.engine: Engine = create_engine(self.connection_string)
        self.session: Session = Session(self.engine)

    def execute_select_query(self, query: Select):
        return self.session.query(query)

    def execute_insert_query(self, query: Insert):
        self.session.query(query)
        self.session.commit()

