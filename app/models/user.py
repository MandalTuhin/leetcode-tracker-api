from typing import Annotated

from pydantic import StringConstraints
from sqlmodel import Field, SQLModel

PasswordStr = Annotated[str, StringConstraints(max_length=72, min_length=8)]


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str


class UserCreate(SQLModel):
    username: str = Field(index=True, unique=True)
    password: PasswordStr


class Token(SQLModel):
    access_token: str
    token_type: str
