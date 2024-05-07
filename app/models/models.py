from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class Task(Base):
    __tablename__='tasks'

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(50))
    task_description = Column(String(100))
