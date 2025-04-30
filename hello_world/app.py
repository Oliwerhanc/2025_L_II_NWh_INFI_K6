from fastapi import FastAPI
from hello_world.views import hello_world

app = FastAPI()
app.include_router(hello_world)
