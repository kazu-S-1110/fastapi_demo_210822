from typing import Optional
from pydantic import BaseModel, Field


class TaskBase(BaseModel):  # 共通部分をクラス化
    title: Optional[str] = Field(None, example="I will do something.")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="Complete Flag")

    class Config:  # DBと接続する際に使用
        orm_mode = True
