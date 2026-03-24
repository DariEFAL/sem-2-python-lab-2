from __future__ import annotations

from enum import Enum
from typing import Union, Optional, Dict, Type
from src.error.task_errors import PriorityInvalidError, PriorityTypeError


class Priority(Enum):
    """Приоритеты задачи"""
    LOW = "низкий"
    MEDIUM = "средний"
    HIGH = "высокий"

    def __str__(self) -> str:
        return self.value

class PriorityDescriptor:
    """Дата-дескриптор priority. Если ничего не присваивать, то по умолчанию priority=средний"""
    def __init__(self):
        self._storage: Dict[object, Priority] = {}

    def __set__(self, obj: object, value: Union[Priority, str, None]) -> None:
        if value is None:
            self._storage[obj] = Priority.MEDIUM
        elif isinstance(value, Priority):
            self._storage[obj] = value
        else:
            try:
                self._storage[obj] = Priority(value.lower())
            except AttributeError:
                raise PriorityTypeError(type(value))
            except ValueError:
                raise PriorityInvalidError(value, allowed_values=[i.value for i in Priority])
        
    def __get__(self, obj: object, objtype: Optional[Type] = None) -> Union[PriorityDescriptor, Priority]:
        if obj is None:
            return self
        
        return Priority(self._storage[obj])