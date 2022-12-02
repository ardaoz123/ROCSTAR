from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_user,
    delete_user,
    retrieve_users,
    retrieve_user,
    update_user,
)
from ..models.user import(
    ErrorResponseModel,
    ResponseModel,
    Users,
    UpdateUsers,
)

router = APIRouter()

@router.post("/", response_description="User data added into the database")
async def add_user_data(user: Users = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)  # type: ignore
    return ResponseModel(new_user, "user added successfully.")

@router.get("/", response_description="users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")

@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUsers = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "user with ID: {} info update is successful".format(id),
            "user's information updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )
    
@router.delete("/{id}", response_description="user data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )