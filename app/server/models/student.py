#import libraries
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

#define model named students
class Students(BaseModel):
    fullName: str = Field(...)
    email: EmailStr = Field(...)
    year: int = Field(..., gt=0, lt=9)
    
    class Config:
        schema_extra = {
            "example": {
                "fullName": "John Doe",
                "email": "example@example.xx",
                "year": 2,
            }
        }
        
#define model named students
class UpdateStudents(BaseModel):
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    year: int = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2
            }
        }