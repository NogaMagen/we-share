from fastapi import FastAPI

from controllers.user import UserController

app = FastAPI()

user_controller = UserController()

app.include_router(user_controller.router)
