from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db

# Initialize the router
router = APIRouter(
    prefix="/students",
    tags=["students"]
)

# Define the routes for getting the students list
@router.get("/list", response_model=List[schemas.StudentBase])
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

# Define the routes for creating a student
@router.post("/create", response_model=schemas.StudentBase)
def create_student(student: schemas.StudentBase, db: Session = Depends(get_db)):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Define the routes for updating a student
@router.put("/update/{student_id}", response_model=schemas.StudentBase)
def update_student(student_id: int, student: schemas.StudentBase, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    for key, value in student.model_dump().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

# Define the routes for deleting a student
@router.delete("/delete/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return