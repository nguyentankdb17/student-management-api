from datetime import date
from pydantic import BaseModel

class StudentBase(BaseModel):
    id: int
    name: str
    gender: str
    dob: date
    university: str

    class Config:
        orm_mode = True


class CreateStudent(StudentBase):
    class Config:
        orm_mode = True