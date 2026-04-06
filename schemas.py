from pydantic import BaseModel
from typing import List

# RECORD
class RecordBase(BaseModel):
    title: str
    amount: float

class RecordCreate(RecordBase):
    pass

class Record(RecordBase):
    id: int

    class Config:
        from_attributes = True


# USER
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    records: List[Record] = []

    class Config:
        from_attributes = True