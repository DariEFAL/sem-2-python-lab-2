from __future__ import annotations

from enum import Enum
from typing import Union, Dict


class Priority(Enum):
    """Приоритеты задачи"""
    LOW = "низкий"
    MEDIUM = "средний"
    HIGH = "высокий"

    def __str__(self):
        return self.value

class PriorityDescriptor:
    def __init__(self):
        self._storage: Dict[object, Priority] = {}

    def __set__(self, obj, value: Union[Priority, str, None]):
        if value is None:
            self._storage[obj] = Priority.MEDIUM
        elif isinstance(value, Priority):
            self._storage[obj] = value
        else:
            try:
                self._storage[obj] = Priority(value.lower())
            except AttributeError:
                raise TypeError(f"Неверный тип: {type(value)}")
            except ValueError:
                raise ValueError(f"Недопустимый приоритет: {value}")
        
    def __get__(self, obj, objtype=None) -> Union[PriorityDescriptor, Priority]:
        if obj is None:
            return self
        
        return Priority(self._storage[obj])