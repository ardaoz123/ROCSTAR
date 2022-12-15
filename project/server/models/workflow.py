# import libraries
from typing import Optional, Union, Any
from pydantic import BaseModel, Field, EmailStr
from beanie import Document


class Workflows(Document):
    isComplete: bool
    summary: Union[str, None] = None
    owner_id: Union[str, None] = None
    priority: int

    class Config:
        schema_extra = {
            "example": {
                "fullName": "",
                "email": "",
                "age": "",
                "student": "",
                "is_teacher": "",
                "is_admin": "",
                "schoolYear": ""
            }
        }


# define model named students
class UpdateWorkflow(BaseModel):
    isComplete: Optional[bool]
    summary: Optional[str]
    owner_id: Optional[str]
    priority: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "fullName": "",
                "email": "",
                "age": "",
                "student": "",
                "is_teacher": "",
                "is_admin": "",
                "schoolYear": ""
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
