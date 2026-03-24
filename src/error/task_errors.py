class TaskError(Exception):
    """Базовое исключение для всех ошибок, связанных с задачами"""
    pass


class IdError(TaskError):
    """Базовое исключение для ошибок ID"""
    pass

class IdDuplicateError(IdError):
    """Исключение: ID уже существует"""
    def __init__(self, value):
        self.value = value
        super().__init__(f"ID '{value}' уже используется. ID должны быть уникальными.")


class TextError(TaskError):
    """Базовое исключение для ошибок текста"""
    pass

class TextEmptyError(TextError):
    """Исключение: текст не может быть пустым"""
    def __init__(self):
        super().__init__("Описание задачи не может быть пустым. Укажите непустую строку.")

class TextTypeError(TextError):
    """Исключение: неверный тип текста"""
    def __init__(self, type):
        self.type = type
        super().__init__(f"Описание задачи должно быть строкой (str), получен {type.__name__}")


class PriorityError(TaskError):
    """Базовое исключение для ошибок приоритета"""
    pass

class PriorityInvalidError(PriorityError):
    """Исключение: недопустимое значение приоритета"""
    def __init__(self, value, allowed_values=None):
        self.value = value
        self.allowed_values = allowed_values or ["низкий", "средний", "высокий"]
        super().__init__(
            f"Недопустимый приоритет: '{value}'. "
            f"Допустимые значения: {", ".join(self.allowed_values)}"
        )

class PriorityTypeError(PriorityError):
    """Исключение: неверный тип приоритета"""
    def __init__(self, type):
        self.type = type
        super().__init__(
            f"Приоритет должен быть Priority, str или None, "
            f"получен {type.__name__}"
        )


class StatusError(TaskError):
    """Базовое исключение для ошибок статуса"""
    pass

class StatusInvalidError(StatusError):
    """Исключение: недопустимое значение статуса"""
    def __init__(self, value, allowed_values=None):
        self.value = value
        self.allowed_values = allowed_values or ["pending", "in_progress", "completed"]
        super().__init__(
            f"Недопустимый статус: '{value}'. "
            f"Допустимые значения: {", ".join(self.allowed_values)}"
        )

class StatusTypeError(StatusError):
    """Исключение: неверный тип статуса"""
    def __init__(self, type):
        self.type = type
        super().__init__(
            f"Статус должен быть Status, str или None, "
            f"получен {type.__name__}"
        )


class TaskStatusError(TaskError):
    """Исключение: недопустимая операция для текущего состояния задачи"""
    def __init__(self, current_status):
        self.current_status = current_status
        super().__init__(f"Нельзя применить операцию на задачу в статусе '{current_status}'")
