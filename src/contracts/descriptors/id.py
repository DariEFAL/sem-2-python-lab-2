from __future__ import annotations

from uuid import uuid4
from typing import Union, Dict, Set


class IdDescriptor:
    def __init__(self):
        self._storage: Dict[object, str] = {}
        self._used_ids: Set[str] = set()

    def __set__(self, obj, value: Union[None, str, int]):
        if value is None:
            value = str(uuid4())

            while value in self._used_ids:
                value = str(uuid4())
        else:
            value = str(value)

            if value in self._used_ids:
                raise ValueError(f"ID {value} уже используется")
            
        self._used_ids.add(value)
        self._storage[obj] = value

    def __get__(self, obj, objtype=None) -> Union[IdDescriptor, str]:
        if obj is None:
            return self

        return self._storage[obj]
        


