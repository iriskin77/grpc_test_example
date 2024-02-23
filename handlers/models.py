from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, Date
from core.base import Base


class Todo(Base):

    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    completed = Column(Boolean, default=False)
    day = Column(Integer, default=0)
