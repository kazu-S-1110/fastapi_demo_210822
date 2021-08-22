from sqlalchemy import Column, Interger, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Interger, primary_key=True)
    title = Column(String(1024))

    done = relationship("Done", back_populates="tasks")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Interger, ForeignKey("tasks.id", primary_key=True))

    task = relationship("Task", back_populates="done")
