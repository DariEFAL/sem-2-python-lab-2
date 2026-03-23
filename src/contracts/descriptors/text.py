from __future__ import annotations

from typing import Union, Optional, Dict


class TextDescriptor:
    def __init__(self):
        self._storage: Dict[str] = {}
    
    def __set__(self, obj, new_text: Optional[str]):
        if new_text is None:
            self._storage[obj] = ""
        elif isinstance(new_text, str):
            self._storage[obj] = new_text
        else:
            raise TypeError(f"Неверный тип: {type(new_text)}")


    def __get__(self, obj, objtype=None) -> Union[TextDescriptor, str]:
        if obj is None:
            return self
        
        return self._storage[obj]

