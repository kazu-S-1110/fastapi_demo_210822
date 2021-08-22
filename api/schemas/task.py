from typing import Optional
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="Complete react")
    done: bool = Field(False, description="Complete Flag")
