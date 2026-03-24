import sys

from dataclasses import dataclass
from typing import TextIO
from collections.abc import Iterable

from src.contracts.task import Task
from src.logging import logging_result


def check_stdin(task: list[str], line_number: int) -> dict[str, str]:
    """Проверяет данные, которые ввел пользователь"""
    try:
        dict = {}

        for i in task:
             key, value = i.split(":")
             if key not in ("text", "priority", "status"):
                  raise ValueError
             dict[key] = value

        return dict
    except ValueError:
        logging_result(False, id=None, error_text=f"Неправильный ввод stdin в строке {line_number}: задача может состоять только из двух аргументов: id и text")
        print(f"Неправильный ввод stdin в строке {line_number}: задача может состоять только из двух аргументов: id и text")
        return {"error": f"Неправильный ввод stdin в строке {line_number}: задача может состоять только из двух аргументов: id и text"}


@dataclass(frozen=True)
class StdinSource:
    stream: TextIO = sys.stdin
    name: str = "stdin"

    def get_tasks(self) -> Iterable[Task]:
        """
        Возвращает задачи полученные из stdin. Пользователь вводит строго сначала имя поля, потом его значение через : : text:текст priority:приоритет status:статус
        :param argumentes: None
        :return: Iterable[Task]
        """
        for line_number, line in enumerate(self.stream):

            line = line.strip()

            if not line:
                continue

            line = line.split()

            task = check_stdin(line, line_number)
            if "error" in task:
                    continue
                
            task_text = task.get("text", None)
            task_priority = task.get("priority", None)
            task_status = task.get("status", None)
            
            yield Task(
                text=task_text, priority=task_priority, status=task_status
            )