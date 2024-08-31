from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from services.user import AuthService
from settings.consts import Authentication

user_router = APIRouter

auth_service = AuthService(connection_string=Authentication.USERS_CONNECTION_STRING)


class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/signup", self.sign_up, methods=["POST"])
        self.router.add_api_route("/login", self.log_in, methods=["POST"])

    @staticmethod
    async def sign_up(email: EmailStr, password: str):
        result = auth_service.sign_up(email=email, password=password)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @staticmethod
    async def log_in(email: EmailStr, password: str):
        result = auth_service.log_in(email=email, password=password)
        if "error" in result:
            raise HTTPException(status_code=401, detail=result["error"])
        return result
