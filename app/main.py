from fastapi import FastAPI
from app.api.controllers import users
from app.db.base import init_db

app = FastAPI(title="User CRUD API")

init_db()  # cria as tabelas

app.include_router(users.router)
