from pydantic import BaseModel

class Problem(BaseModel):
    id: int
    title: str
    difficulty: str
    tags: list[str] = []
    solution_cpp: str | None = None