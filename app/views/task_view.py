from fastapi import APIRouter, Depends
from app.controller.task_controller import TasksController
from app.models.task_model import Task

router = APIRouter()
task_controller = TasksController()

# Route to create an task
@router.post("/tasks/", response_model=Task)
def create_task(task: Task):
    return task_controller.create_task(task)

# Route to read an task
@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    return task_controller.read_task(task_id)

# Route to update an task
@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    return task_controller.update_task(task_id, task)

# Route to delete an task
@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    return task_controller.delete_task(task_id)
