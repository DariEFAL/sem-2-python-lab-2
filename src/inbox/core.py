from collections.abc import Sequence, Iterable

from src.contracts.task_source import TaskSource
from src.contracts.task import Task
from src.logging import logging_result
from src.error.sources_error import InvalidSourceError


class InboxApp:
    def __init__(self, sources: Sequence[TaskSource] = None):
        self.sources = sources or []

    def iter_task(self) -> Iterable[Task]:
        """
        Возвращает задачи из разных источников
        :param argumentes: None
        :return: Iterable[Task]
        """
        for source in self.sources:
            if not isinstance(source, TaskSource):
                raise InvalidSourceError(type(source))
            
            for task in source.get_tasks():
                yield task