from __future__ import annotations

from typing import Union, Dict
from src.error.task_errors import TextEmptyError, TextTypeError


class TextDescriptor:
    """Дата-дескриптор text. Это обязательное поле. Нельзя оставить пустым."""
    def __init__(self):
        self._storage: Dict[str] = {}
    
    def __set__(self, obj, new_text: str):
        if new_text is None or new_text == "":
           raise TextEmptyError()
        elif isinstance(new_text, str):
            self._storage[obj] = new_text
        else:
            raise TextTypeError(type(new_text))


    def __get__(self, obj, objtype=None) -> Union[TextDescriptor, str]:
        if obj is None:
            return self
        
        return self._storage[obj]

