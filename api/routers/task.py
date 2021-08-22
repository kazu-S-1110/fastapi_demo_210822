from fastapi import APIRouter
from typing import List
import api.schemas.task as task_schema  # modelsのものはtask_modelとして区別するために読み替えてimportする

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="first task")]


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    # **を使用してキーワード引数として展開、つまり**task_body.dict()はtitle=task_body.title, done=task_body.doneになる
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass
