from typing import Optional, List


class SourceError(Exception):
    pass


class InvalidFieldError(SourceError):
    """Неизвестное поле в источнике подачи заданий stdin"""
    def __init__(self, field: str, line: int, allowed_fields: Optional[List[str]] = None):
        self.field = field
        self.line = line
        self.allowed_fields = allowed_fields or ["text", "priority", "status"]
        super().__init__(f"Неизвестное поле: '{field}' в {line}. Допустимые поля: {", ".join(allowed_fields)}")


class InvalidSourceError(SourceError):
    """Недопустимый тип источника"""
    def __init__(self, source: str):
        self.source = source
        super().__init__(f"Недопустимый тип источника: '{source}' в . Допустимый тип TaskSource.")