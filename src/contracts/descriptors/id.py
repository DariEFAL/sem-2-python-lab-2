from __future__ import annotations

from uuid import uuid4
from typing import Union, Optional, Dict, Set, Type
from src.error.task_errors import IdDuplicateError


class IdDescriptor:
    """Дата-дескриптор id. Можно присваивать только уникальные id."""
    def __init__(self):
        self._storage: Dict[object, str] = {}
        self._used_ids: Set[str] = set()

    def __set__(self, obj: object, value: Union[None, str, int]) -> None:
        if value is None or value == "":
            value = str(uuid4())

            while value in self._used_ids:
                value = str(uuid4())
        else:
            value = str(value)

            if value in self._used_ids:
                raise IdDuplicateError(value)
            
        self._used_ids.add(value)
        self._storage[obj] = value

    def __get__(self, obj: object, objtype: Optional[Type] = None) -> Union[IdDescriptor, str]:
        if obj is None:
            return self

        return self._storage[obj]
        


