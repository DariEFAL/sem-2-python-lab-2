from typing import Union
from datetime import datetime
#src.contracts.
from descriptors.id import IdDescriptor
from descriptors.text import TextDescriptor
from descriptors.priority import Priority, PriorityDescriptor
from descriptors.status import Status, StatusDescriptor


class Task:
    __slots__ = ()

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

    



