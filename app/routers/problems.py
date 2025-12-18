from fastapi import APIRouter
from app.models.problem import Problem

router = APIRouter(prefix="/problems", tags=["Problems"])

db: list[Problem] = []

@router.post("/")
async def add_problem(problem: Problem):
    db.append(problem)
    return {"message" : "Problem added!", "count": len(db)}

@router.get("/")
async def get_problems() -> list[Problem]:
    return db