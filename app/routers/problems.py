from fastapi import APIRouter
from app.models.problem import Problem
from app.core.types import unordered_map

router = APIRouter(prefix="/problems", tags=["Problems"])

db: list[Problem] = []
db: unordered_map[int, Problem] = {}

@router.post("/")
async def add_problem(problem: Problem):
    db.append(problem)
    db[problem.id] = problem
    return {"message" : "Problem added!", "count": len(db)}

# @router.get("/")
# async def get_problems() -> unordered_map[int, Problem]:
#     return db

@router.get("/")
async def get_problems() -> list[Problem]:
    return db