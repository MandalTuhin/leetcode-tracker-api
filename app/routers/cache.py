from fastapi import APIRouter, HTTPException

from app.core.types import unordered_map
from app.models.problem import Problem

router = APIRouter(prefix="/cache", tags=["Cache"])


CAPACITY = 3

lru_cache: unordered_map[int, Problem] = {}


@router.put("/{problem_id}")
async def acess_problem(problem_id: int, problem: Problem):
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    if problem_id != problem.id:
        raise HTTPException(status_code=500, detail="Problem ID mismatch")

    """
    Simulates accessing or adding a problem to the LRU Cache.
    If the key exists, we move it to the end (most recent).
    If it's new and we are at capacity, we pop the first item (least recent).
    """

    if problem.id in lru_cache:
        # Key esists: Remove it so we can re-insert it at the end
        # (Equivalent to moving a node to the front of a linked list)
        del lru_cache[problem_id]
    elif len(lru_cache) >= CAPACITY:
        # Cache is full: Remove the least recently used item
        # (Equivalent to removing the tail of a linked list)
        oldest_key = next(iter(lru_cache))
        del lru_cache[oldest_key]

    lru_cache[problem_id] = problem
    return {"message": "Cache updated", "current_cache": list(lru_cache.keys())}
