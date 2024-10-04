from functools import lru_cache

from passlib.hash import bcrypt
from pydantic import EmailStr

from data_layer.user import UserDataLayer


class AuthService(UserDataLayer):
    def __init__(self, connection_string: str):
        super().__init__(connection_string)

    def sign_up(self, email: EmailStr | None, password: str | None) -> dict:
        fetched_user = self.get_user_by_email(email=email)
        if fetched_user:
            return {"error": "email already registered"}

        hashed_password = bcrypt.hash(password)
        new_user = self.create_user(email=email, password=hashed_password)
        return {"message": "User created", "user": new_user.email}

    @lru_cache(maxsize=None)
    def log_in(self, email: EmailStr, password: str | None) -> dict:
        user = self.get_user_by_email(email)
        if not user:
            return {"error": "User not found"}

        if not bcrypt.verify(password, user.password):
            return {"error": "Invalid credentials"}

        return {"message": "Login successful", "user": user.email}
