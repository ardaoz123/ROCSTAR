from fastapi import APIRouter, Body

from beanie import PydanticObjectId

from ..database import (
    get_workflow,
)

from ..models.workflow import (
    Response,
    Workflows,
    UpdateWorkflow,
)

router = APIRouter()


@router.get("/{id}", response_description="workflow data retrieved", response_model=Response)
async def get_workflow_data(workflow_id: PydanticObjectId):
    workflow = await get_workflow(workflow_id)
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
