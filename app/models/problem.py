from enum import Enum
from app.core.types import binary
from sqlmodel import Field, SQLModel


class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    DIFFICULT = "Difficult"  # I am adding "difficult" for now, I may change it later.


class ProblemBase(SQLModel):
    problem_no: int = Field(unique=True, index=True)
    title: str = Field(index=True)
    difficulty: Difficulty
    solution_cpp: str | None = None
    is_solved: binary = Field(default=False)


class ProblemCreate(ProblemBase):
    pass


class Problem(ProblemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
