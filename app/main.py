from fastapi import FastAPI

from app.users.router import router as router_user

app = FastAPI()

app.include_router(router_user)

@app.get("/")
async def root():
    return {"message": "Hello World"}