from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM


Tortoise.init_models(["src.database.models"], "models")

from src.routes import users, works, authors, authors_works

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(works.router)
app.include_router(authors.router)
app.include_router(authors_works.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)
app.mount("/static", StaticFiles(directory="C:\\Users\\Yana\\Desktop\\New"), name="static")

@app.get("/")
def home():
    return "Hello, World!"
