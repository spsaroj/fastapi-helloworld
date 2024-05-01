from fastapi import HTTPException
from app.models.task_model import Task
from app.models.dbconnection import conn

class TasksController:
    @staticmethod
    def create_task(task: Task):
        cursor = conn.cursor()
        query = "INSERT INTO tasks (name, description) VALUES (%s, %s)"
        cursor.execute(query, (task.name, task.description))
        conn.commit()
        task.id = cursor.lastrowid
        cursor.close()
        return task

    @staticmethod
    def read_task(task_id: int):
        cursor = conn.cursor()
        query = "SELECT id, name, description FROM tasks WHERE id=%s"
        cursor.execute(query, (task_id,))
        task = cursor.fetchone()
        cursor.close()
        if task is None:
            raise HTTPException(status_code=404, detail="task not found")
        return {"id": task[0], "name": task[1], "description": task[2]}

    @staticmethod
    def update_task(task_id: int, task: Task):
        cursor = conn.cursor()
        query = "UPDATE tasks SET name=%s, description=%s WHERE id=%s"
        cursor.execute(query, (task.name, task.description, task_id))
        conn.commit()
        cursor.close()
        task.id = task_id
        return task

    @staticmethod
    def delete_task(task_id: int):
        cursor = conn.cursor()
        query = "DELETE FROM tasks WHERE id=%s"
        cursor.execute(query, (task_id,))
        conn.commit()
        cursor.close()
        return {"id": task_id}
