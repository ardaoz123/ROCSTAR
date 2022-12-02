#import libraries
from typing import Optional, Union, List
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

#define model named users
class Users(BaseModel):
    fullName: str = Field(...)
    email: EmailStr = Field(...)
    schoolYear: int = Field(gt=0, lt=9)
    function: str = Field(...)
    age: int = Field(..., gt=0, lt=99)
    
    class Config:
        schema_extra = {
            "example": {
                "fullName": "John Doe",
                "email": "example@example.xx",
                "schoolYear": "",
                "function": "Student or staff",
                "age": ""
            }
        }
        
#define model named students
class UpdateUsers(BaseModel):
    fullName: Optional[str]
    email: Optional[EmailStr]
    schoolYear: Optional[int]
    function: Optional[str]
    age: Optional[int]
    
    class Config:
        schema_extra = {
            "example": {
                "fullName": "John Doe",
                "email": "example@example.xx",
                "schoolYear": "",
                "function": "Student or staff",
                "age": ""
            }
        }
        
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}