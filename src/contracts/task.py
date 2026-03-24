from typing import Union
from datetime import datetime, timedelta

from src.contracts.descriptors.id import IdDescriptor
from src.contracts.descriptors.text import TextDescriptor
from src.contracts.descriptors.priority import Priority, PriorityDescriptor
from src.contracts.descriptors.status import Status, StatusDescriptor
from src.error.task_errors import TaskStatusError


class Task:
    id = IdDescriptor()
    text = TextDescriptor()
    priority = PriorityDescriptor()
    status = StatusDescriptor()

    __slots__ = ('_creation_time',)

    def __init__(self, *, 
                 text: str, 
                 id: Union[str, int] = None, 
                 priority: Union[Priority, str] = None, 
                 status: Union[Status, str] = None):
        
        self.id = id
        self.text = text
        self.priority = priority
        self.status = status
        self._creation_time = datetime.now()

    @property
    def creation_time(self):
        """Время создания (только для чтения)"""
        return self._creation_time

    @property
    def age(self) -> timedelta:
        """Сколько прошло времени с момента создания задачи"""
        return datetime.now() - self.creation_time
    
    def start(self):
        """Начать выполнение задачи"""
        if self.status != Status.PENDING:
            raise TaskStatusError(self.status)
        
        self.status = Status.IN_PROGRESS
    
    def complete(self):
        """Завершить задачу"""
        if self.status == Status.COMPLETED:
            raise TaskStatusError(self.status)
        
        self.status = Status.COMPLETED

    def __str__(self):
        return f"[{self.creation_time} | {self.status} | {self.priority}] {self.text}"
    

    



