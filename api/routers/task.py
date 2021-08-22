from fastapi import APIRouter
from typing import List
import api.schemas.task as task_schema  # modelsのものはtask_modelとして区別するために読み替えてimportする

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="first task")]


@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass