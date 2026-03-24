import sys

from dataclasses import dataclass
from typing import TextIO
from collections.abc import Iterable

from src.contracts.task import Task
from src.logging import logging_result
from src.error.sources_error import InvalidFieldError


def check_stdin(task: list[str], line_number: int) -> dict[str, str]:
    """Проверяет данные, которые ввел пользователь"""
    dict = {}

    for i in task:
        key, value = i.split("=")
        if key not in ("text", "priority", "status"):
            raise InvalidFieldError(key, line_number)
        dict[key] = value

    return dict


@dataclass(frozen=True)
class StdinSource:
    stream: TextIO = sys.stdin
    name: str = "stdin"

    def get_tasks(self) -> Iterable[Task]:
        """
        Возвращает задачи полученные из stdin. Пользователь вводит строго сначала имя поля, потом его значение через "=". 
        А между полями " ;; ": text=текст ;; priority=приоритет ;; status=статус. Чтобы закончить ввод ввести cntr+D.
        :param argumentes: None
        :return: Iterable[Task]
        """
        for line_number, line in enumerate(self.stream, start=1):

            line = line.strip()

            if not line:
                continue

            line = line.split(" ;; ")

            try:
                task = check_stdin(line, line_number)
            except Exception as e:
                logging_result(False, error_text=str(e))
                continue
            
            task_text = task.get("text", None)
            task_priority = task.get("priority", None)
            task_status = task.get("status", None)

            try:
                task = Task(text=task_text, priority=task_priority, status=task_status)
            except Exception as e:
                logging_result(False, name_source=self.name, error_line=line_number, error_text=str(e))
                continue
            
            yield task