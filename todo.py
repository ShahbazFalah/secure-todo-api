from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()


class TaskIn(BaseModel):
  title: str = Field(min_length=3, max_length=50)
  description: Optional[str] = None
  priority: int = Field(ge=1, le=5)
  internal_note: str


class TaskOut(BaseModel):
  id: int
  title: str
  description: Optional[str] = None
  priority: int
  is_completed: bool = False


# دیتابیس فرضی در حافظه
task_db = {}


@app.post(
    "/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskIn):
  task_id = len(task_db) + 1

  new_task = {
      "id": task_id,
      "title": task.title,
      "description": task.description,
      "priority": task.priority,
      "is_completed": False,
      "internal_note": task.internal_note,
  }

  task_db[task_id] = new_task
  return new_task


@app.get("/tasks/{task_id}", response_model=TaskOut)
async def get_task(task_id: int):
  if task_id not in task_db:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task with the requested ID was not found.",
    )
  return task_db[task_id]


@app.patch("/tasks/{task_id}/complete", response_model=TaskOut)
async def complete_task(task_id: int):
  if task_id not in task_db:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task with the requested ID was not found.",
    )

  task = task_db[task_id]

  if task["is_completed"]:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="This task has already been marked as completed.",
    )

  task["is_completed"] = True
  return task