from fastapi import APIRouter, Body

from beanie import PydanticObjectId

from ..database import (
    update_user_data,
    delete_user,
    get_user,
    get_all_users,
    add_new_user,
)

from ..models.user import (
    Response,
    Users,
    UpdateUsers,
)

router = APIRouter()


@router.post("/", response_description="User data added into the database")
async def add_user(user: Users = Body(...)):
    new_user = await add_new_user(user)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_user
    }


@router.get("/", response_description="All users retrieved")
async def users():
    all_users = await get_all_users()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Students data retrieved successfully",
        "data": all_users
    }


@router.get("/{id}", response_description="User data retrieved", response_model=Response)
async def get_user_data(user_id: PydanticObjectId):
    student = await get_user(user_id)
    if student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student data retrieved successfully",
            "data": student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student doesn't exist",
    }


@router.put("/{id}", response_model=Response, response_description="User data updated")
async def update_user(user_id: PydanticObjectId, req: UpdateUsers = Body(...)):
    updated_user = await update_user_data(user_id, req.dict())
    if updated_user:
        return {
            "code": 200,
            "message": "success",
            "description": "Student with ID: {} updated".format(id),
            "data": updated_user
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Student with ID: {} not found".format(id),
        "data": False
    }


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(user_id: PydanticObjectId):
    deleted_student = await delete_user(user_id)
    if deleted_student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student with ID: {} removed".format(id),
            "data": deleted_student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student with id {0} doesn't exist".format(id),
        "data": False
    }
