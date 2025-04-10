from database import Base
from sqlalchemy import Column, Integer, String, DATE, Enum as SqlEnum
import enum

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dob = Column(DATE, nullable=False)
    university = Column(String, nullable=False)
