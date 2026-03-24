from __future__ import annotations

from enum import Enum
from typing import Union, Dict
from src.error.task_errors import StatusInvalidError, StatusTypeError


class Status(Enum):
    PENDING = "ожидает"
    IN_PROGRESS = "в процессе"
    COMPLETED = "выполнено"

    def __str__(self):
        return self.value
    
class StatusDescriptor:
    """Дата-дескриптор status. Если ничего не присваивать, то по умолчанию status=ожидает"""
    def __init__(self):
        self._storage: Dict[object, Status] = {}

    def __set__(self, obj, value: Union[Status, str, None]):
        if value is None:
            self._storage[obj] = Status.PENDING
        elif isinstance(value, Status):
            self._storage[obj] = value
        else:
            try:
                self._storage[obj] = Status(value.lower())
            except AttributeError:
                raise StatusTypeError(type(value))
            except ValueError:
                raise StatusInvalidError(value, allowed_values=[i.value for i in Status])
            
    def __get__(self, obj, objtype=None) -> Union[StatusDescriptor, Status]:
        if obj is None:
            return self
        
        return self._storage[obj]
