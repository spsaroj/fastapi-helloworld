from pydantic import BaseModel

class Task(BaseModel):
    task_name: str
    task_description: str = None