import sqlalchemy
from fastapi import FastAPI
from src.sql.database import engine
from src.api.router import APIrouter
from src.sql import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)