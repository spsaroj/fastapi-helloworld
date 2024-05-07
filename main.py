from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import app.models.models as models
from app.models.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class TaskBase(BaseModel):
    task_name: str
    task_description: str

class TaskUpdate(TaskBase):
    pass

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/tasks/", status_code=status.HTTP_200_OK)
async def read_tasks(db: db_dependency):
    task = db.query(models.Task).all()
    return task

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
async def create_tasks(tasks: TaskBase, db: db_dependency):
    db_task = models.Task(**tasks.dict())
    db.add(db_task)
    db.commit()


@app.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def read_tasks(task_id:int, db: db_dependency):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def delete_tasks(task_id:int, db: db_dependency):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    db.delete(task)
    db.commit()

@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task_data: TaskUpdate, db: db_dependency):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")

    for field, value in task_data.dict().items():
        if value is not None:
            setattr(task, field, value)

    db.commit()
    return task