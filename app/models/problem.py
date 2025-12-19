from enum import Enum

from pydantic import computed_field
from sqlmodel import Field, SQLModel

from app.core.types import binary


class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    DIFFICULT = "Difficult"  # I am adding "difficult" for now, I may change it later.


class ProblemBase(SQLModel):
    problem_no: int = Field(unique=True, index=True)
    title: str = Field(index=True)
    difficulty: Difficulty
    solution_cpp: str | None = None
    slug: str | None = Field(default=None, index=True)
    is_solved: binary = Field(default=False)


class ProblemUpdate(SQLModel):
    """
    Model for partial updates via PATCH.
    """

    title: str | None = None
    difficulty: Difficulty | None = None
    solution_cpp: str | None = None
    slug: str | None = None
    is_solved: binary | None = None


class ProblemCreate(ProblemBase):
    pass


class Problem(ProblemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    @computed_field
    @property
    def leetcode_url(self) -> str:
        """
        Dynamic URL construction from slug
        """
        if self.slug:
            return f"https://leetode.com/problems/{self.slug}"
        return ""
