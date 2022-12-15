from typing import List, Union
import motor.motor_asyncio
from decouple import config
from beanie import init_beanie, PydanticObjectId
from .models.workflow import Workflows
from .models.user import Users
from fastapi import HTTPException

# MongoDB URI to connect to the MongoDB cluster
MONGODB_URL = config('MONGODB_DETAILS')


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
    await init_beanie(database=client.ROCSTAR, document_models=[Users])
    await init_beanie(database=client.todo, document_models=[Workflows])


# Helper methods to get instances
async def get_workflow(workflow_id: PydanticObjectId) -> Workflows:
    workflow = await Workflows.get(workflow_id)
    if workflow:
        return workflow


async def get_user(user_id: PydanticObjectId) -> Users:
    user = await Users.get(user_id)
    if user:
        return user


async def get_all_users() -> List[Users]:
    users = await Users.all().to_list()
    if not users:
        raise HTTPException(
            status_code=404,
            detail="No users found"
        )
    return users


async def add_new_user(new_user: Users) -> Users:
    user = await new_user.create()
    return user


async def update_user_data(user_id: PydanticObjectId, data: dict) -> Union[bool, Users]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    user = await Users.get(user_id)

    if user:
        await user.update(update_query)
        return user

    raise HTTPException(
        status_code=404,
        detail="No users found"
    )


async def delete_user(user_id: PydanticObjectId) -> bool:
    student = await Users.get(user_id)
    if student:
        await student.delete()
        return True
