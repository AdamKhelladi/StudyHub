from fastapi import FastAPI
from app.database import Base, engine 
from app import models

app = FastAPI()

