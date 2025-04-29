from fastapi import APIRouter

hello_world = APIRouter()

@hello_world.get("/")
async def index():
    return {"message": "Hello, World!"}
