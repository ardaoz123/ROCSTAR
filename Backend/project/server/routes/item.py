from fastapi import APIRouter, Body

from beanie import PydanticObjectId

from ..database import (
    get_all_items,
)

from ..models.Item import (
    Response,
    Item,
    UpdateItem,
)

router = APIRouter()


@router.get("/", response_description="All items retrieved")
async def items():
    all_items = await get_all_items()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "item data retrieved successfully",
        "data": all_items
    }

""""
@router.get("/{id}", response_description="workflow data retrieved", response_model=Response)
async def get_item_data(item_id: PydanticObjectId):
    workflow = await get_workflow(item_id)
    if workflow:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "workflow data retrieved successfully",
            "data": workflow
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "workflow doesn't exist",
    }
"""