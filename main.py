from fastapi import FastAPI
from . import models, database
from .routes import users, records

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(records.router, prefix="/records")


@app.get("/")
def root():
    return {"message": "Finance Backend API Running"}