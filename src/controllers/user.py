from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from services.authentication.user import AuthService
from settings.http_handling import HttpMethod
from settings.systemic import AuthenticationUsingPostgres

user_router = APIRouter

auth_service = AuthService(connection_string=AuthenticationUsingPostgres.USERS_CONNECTION_STRING)


class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/signup", self.sign_up, methods=[HttpMethod.POST])
        self.router.add_api_route("/login", self.log_in, methods=[HttpMethod.POST])

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



