from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True  # Enable compatibility with SQLAlchemy models (ORM)
