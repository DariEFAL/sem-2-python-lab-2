import json

from collections.abc import Iterable
from pathlib import Path
from dataclasses import dataclass
from typing import Dict

from src.contracts.task import Task
from src.logging import logging_result


def parse_json_file(line: str) -> Dict[str, str]:
    """Делает из строки словарь"""
    return json.loads(line)


@dataclass(frozen=True)
class JsonSource:
    path: Path
    name: str = "file-jsonl"

    def get_tasks(self) -> Iterable[Task]:
        """
        Возвращает задачи полученные из jsonl
        :param argumentes: None
        :return: Iterable[Task]
        """
        with self.path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    task = parse_json_file(line)
                except json.JSONDecodeError:
                    logging_result(False, name_source=self.name, error_text=f"Строка {line_number} в {self.path} не является словарем")
                    continue
                
                task_id = task.get("id", None)
                task_text = task.get("text", None)
                task_priority = task.get("priority", None)
                task_status = task.get("status", None)

                try:
                    task = Task(id=task_id, text=task_text, priority=task_priority, status=task_status)
                except Exception as e:
                    logging_result(False, name_source=self.name, error_line=line_number, error_text=str(e))
                    continue

                yield task

