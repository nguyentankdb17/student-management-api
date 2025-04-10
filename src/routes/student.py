from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.StudentBase])
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students
