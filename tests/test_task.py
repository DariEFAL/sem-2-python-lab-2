import pytest
from datetime import datetime, timedelta
from unittest.mock import patch

from src.contracts.task import Task
from src.contracts.descriptors.priority import Priority
from src.contracts.descriptors.status import Status
from src.error.task_errors import TaskStatusError, TaskError


def test_create_task_with_required_fields():
        """Создание задачи только с обязательным полем text"""
        task = Task(text="pampam")
        
        assert task.text == "pampam"
        assert task.id is not None
        assert task.priority == Priority.MEDIUM
        assert task.status == Status.PENDING 
        assert isinstance(task.creation_time, datetime)

def test_create_task_with_all_fields():
        """Создание задачи со всеми полями"""
        task = Task(
            text="Сделать лабу",
            id=42,
            priority=Priority.HIGH,
            status=Status.PENDING
        )
        
        assert task.id == "42"
        assert task.text == "Сделать лабу"
        assert task.priority == Priority.HIGH
        assert task.status == Status.PENDING

def test_create_task_with_string_priority():
        """Создание задачи с приоритетом в виде строки"""
        task = Task(text="Тест", priority="ВЫсокий")
        assert task.priority == Priority.HIGH
    
def test_create_task_with_string_status():
    """Создание задачи со статусом в виде строки"""
    task = Task(text="Тест", status="В процессе")
    assert task.status == Status.IN_PROGRESS

def test_create_task_empty_text_raises_error():
    """Создание задачи с пустым текстом вызывает ошибку"""
    with pytest.raises(TaskError, match="не может быть пустым"):
        Task(text="")

def test_create_task_with_whitespace_text_raises_error(): #????
    """Создание задачи с текстом из пробелов вызывает ошибку"""
    with pytest.raises(TaskError, match="не может быть пустым"):
        Task(text="   ")

def test_create_task_invalid_priority_raises_error():
    """Создание задачи с недопустимым приоритетом вызывает ошибку"""
    with pytest.raises(TaskError, match="Недопустимый приоритет"):
        Task(text="Тест", priority="очень низкий")

def test_create_task_invalid_status_raises_error():
    """Создание задачи с недопустимым статусом вызывает ошибку"""
    with pytest.raises(TaskError, match="Недопустимый статус"):
        Task(text="Тест", status="сомнительный")

def test_change_text():
    """Изменение текста задачи"""
    task = Task(text="Старый текст")
    task.text = "Новый текст"
    assert task.text == "Новый текст"

def test_change_text_empty_raises_error():
    """Изменение текста на пустой вызывает ошибку"""
    task = Task(text="Текст")
    with pytest.raises(TaskError, match="не может быть пустым"):
        task.text = ""

def test_change_priority():
    """Изменение приоритета"""
    task = Task(text="Тест", priority=Priority.LOW)
    task.priority = Priority.HIGH
    assert task.priority == Priority.HIGH

def test_change_priority_with_string():
    """Изменение приоритета через строку"""
    task = Task(text="Тест")
    task.priority = "высокий"
    assert task.priority == Priority.HIGH

def test_change_status():
    """Изменение статуса"""
    task = Task(text="Тест")
    task.status = Status.IN_PROGRESS
    assert task.status == Status.IN_PROGRESS

def test_start_pending_task():
    """Запуск задачи в статусе PENDING"""
    task = Task(text="Тест", status=Status.PENDING)
    task.start()
    assert task.status == Status.IN_PROGRESS

def test_start_already_started_task_raises_error():
    """Запуск уже запущенной задачи вызывает ошибку"""
    task = Task(text="Тест")
    task.start()
    
    with pytest.raises(TaskStatusError, match="Нельзя применить операцию"):
        task.start()

def test_start_completed_task_raises_error():
    """Запуск завершенной задачи вызывает ошибку"""
    task = Task(text="Тест", status=Status.PENDING)
    task.complete()
    
    with pytest.raises(TaskStatusError, match="Нельзя применить операцию"):
        task.start()

def test_complete_in_progress_task():
    """Завершение задачи в статусе IN_PROGRESS"""
    task = Task(text="Тест", status=Status.PENDING)
    task.start()
    task.complete()
    assert task.status == Status.COMPLETED

def test_complete_pending_task():
    """Завершение задачи в статусе PENDING"""
    task = Task(text="Тест", status=Status.PENDING)
    task.complete()
    assert task.status == Status.COMPLETED

def test_complete_already_completed_task_raises_error():
    """Завершение уже завершенной задачи вызывает ошибку"""
    task = Task(text="Тест", status=Status.COMPLETED)
    
    with pytest.raises(TaskStatusError, match="Нельзя применить операцию"):
        task.complete()

def test_age_property():
    """Проверка свойства age (возраст задачи)"""
    with patch('src.contracts.task.datetime') as mock_datetime:
        mock_now = datetime(2024, 1, 15, 10, 0, 0)
        mock_datetime.now.return_value = mock_now
        
        task = Task(text="Тест")
        
        mock_datetime.now.return_value = mock_now + timedelta(seconds=5)
        
        assert task.age.total_seconds() == 5

def test_creation_time_readonly():
    """creation_time только для чтения"""
    task = Task(text="Тест")
    
    with pytest.raises(AttributeError):
        task.creation_time = datetime.now()

