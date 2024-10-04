from pydantic import EmailStr

from .generic import SqlDBDataLayer
from models.user import User


class UserDataLayer(SqlDBDataLayer):
    def __init__(self, connection_string: str):
        super().__init__(connection_string)

    def get_user_by_email(self, email: str) -> User | None:
        return self.session.query(User).filter(User.email == email).first()

    def create_user(self, email: EmailStr, password: str) -> User:
        new_user = User(email=email, password=password)
        self.session.add(new_user)
        self.session.commit()
        return new_user

