from fastapi import APIRouter, Body
from pydantic import Field
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
        "description": "user created successfully",
        "data": new_user
    }


@router.get("/", response_description="All users retrieved")
async def users():
    all_users = await get_all_users()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "user data retrieved successfully",
        "data": all_users
    }


@router.get("/{user_id}", response_description="User data retrieved", response_model=Response)
async def get_user_data(user_id: PydanticObjectId):
    user = await get_user(user_id)
    if user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User data retrieved successfully",
            "data": user
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "user doesn't exist",
    }


@router.put("/{user_id}", response_model=Response, response_description="User data updated")
async def update_user(user_id: PydanticObjectId, req: UpdateUsers = Body(...)):
    updated_user = await update_user_data(user_id, req.dict())
    if updated_user:
        return {
            "code": 200,
            "message": "success",
            "description": "User with ID: {} updated".format(id),
            "data": updated_user
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. User with ID: {} not found".format(id),
        "data": False
    }


@router.delete("/{user_id}", response_description="User data deleted from the database")
async def delete_student_data(user_id: PydanticObjectId):
    deleted_user = await delete_user(user_id)
    if deleted_user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User with ID: {} removed".format(id),
            "data": deleted_user
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "User with id {0} doesn't exist".format(id),
        "data": False
    }
