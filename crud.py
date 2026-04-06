from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password, verify_password

# USER

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user


# RECORD

def create_record(db: Session, record: schemas.RecordCreate, user_id: int):
    db_record = models.Record(**record.dict(), owner_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def get_records(db: Session, user_id: int):
    return db.query(models.Record).filter(models.Record.owner_id == user_id).all()