from collections.abc import Iterable
from dataclasses import dataclass

from src.contracts.task import Task
from src.logging import logging_result


@dataclass(frozen=True)
class GenSource:
    count_gen_tasks: int
    name: str = "gen"

    def get_tasks(self) -> Iterable[Task]:
        """
        Создает задачи и отправляет их
        :param argumentes: None
        :return: Iterable[Task]
        """
        for i in range(1, self.count_gen_tasks + 1):

            task_text = f"Сгенерирована задача номер {i}"

            try:
                task = Task(text=task_text)
            except Exception as e:
                logging_result(False, name_source=self.name, error_line=i, error_text=str(e))
                continue
            
            yield task
