from fastapi import FastAPI

from app.routers import cache, problems

app = FastAPI(title="LeetCode Tracker")

app.include_router(problems.router)
app.include_router(cache.router)


@app.get("/")
async def root():
    return {"status": "System Online"}
