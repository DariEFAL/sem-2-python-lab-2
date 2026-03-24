from typing import Union
from datetime import datetime, timedelta

from src.contracts.descriptors.id import IdDescriptor
from src.contracts.descriptors.text import TextDescriptor
from src.contracts.descriptors.priority import Priority, PriorityDescriptor
from src.contracts.descriptors.status import Status, StatusDescriptor


class Task:
    __slots__ = ('creation_time',)

    id = IdDescriptor()
    text = TextDescriptor()
    priority = PriorityDescriptor()
    status = StatusDescriptor()

    def __init__(self, *, 
                 text: str, 
                 id: Union[str, int] = None, 
                 priority: Union[Priority, str] = None, 
                 status: Union[Status, str] = None):
        
        self.id = id
        self.text = text
        self.priority = priority
        self.status = status
        self.creation_time = datetime.now()

    @property
    def age(self) -> timedelta:
        return datetime.now() - self.creation_time
    

    



