from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_record(record: schemas.RecordCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_record(db, record, user_id)


@router.get("/")
def get_records(user_id: int, db: Session = Depends(get_db)):
    return crud.get_records(db, user_id)