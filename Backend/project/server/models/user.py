# import libraries
from typing import Optional, Union, Any
from pydantic import BaseModel, Field, EmailStr
from beanie import Document
import uuid


class Users(Document):
    uuid: str = Field(default=str(uuid.uuid4()))
    fullName: Union[str, None] = None
    email: Union[str, None] = None
    age: int = Field(gt=12, lt=99)
    is_student: Optional[bool]
    is_teacher: Optional[bool]
    is_admin: Optional[bool]
    schoolYear: Optional[int] = Field(gt=0, lt=6)

    class Config:
        schema_extra = {
            "example": {
                "fullName": "John Doe",
                "email": "example@example.xx",
                "age": "Fill in a number",
                "student": "True or False",
                "is_teacher": "True or False",
                "is_admin": "True or False",
                "schoolYear": "Fill in a number"
            }
        }


# define model named students
class UpdateUsers(BaseModel):
    fullName: Optional[str]
    email: Optional[EmailStr]
    schoolYear: Optional[int]
    age: Optional[int]
    student: Optional[bool]
    is_teacher: Optional[bool]
    is_admin: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "fullName": "John Doe",
                "email": "example@example.xx",
                "schoolYear": "Fill in a number",
                "age": "Fill in a number",
                "student": "True or False",
                "is_teacher": "True or False",
                "is_admin": "True or False",
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }
