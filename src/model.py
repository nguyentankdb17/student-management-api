from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, Enum as SqlEnum
import enum


# Định nghĩa Enum cho SQLAlchemy
class GenderEnum(str, enum.Enum):
    male = "Nam"
    female = "Nữ"


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(SqlEnum(GenderEnum, name="gender_enum"), nullable=False)
    dob = Column(TIMESTAMP, nullable=False)
    university = Column(String, nullable=False)
