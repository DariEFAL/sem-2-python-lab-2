from __future__ import annotations

from typing import Union, Optional, Dict, Type
from src.error.task_errors import TextEmptyError, TextTypeError


class TextDescriptor:
    """Дата-дескриптор text. Это обязательное поле. Нельзя оставить пустым."""
    def __init__(self):
        self._storage: Dict[str] = {}
    
    def __set__(self, obj: object, new_text: str) -> None:
        new_text = new_text.strip()
        
        if new_text is None or new_text == "":
           raise TextEmptyError()
        elif isinstance(new_text, str):
            self._storage[obj] = new_text
        else:
            raise TextTypeError(type(new_text))


    def __get__(self, obj: object, objtype: Optional[Type] = None) -> Union[TextDescriptor, str]:
        if obj is None:
            return self
        
        return self._storage[obj]

