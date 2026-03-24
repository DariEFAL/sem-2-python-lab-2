import logging
from typing import Optional


logging.basicConfig(level=logging.INFO,
                    filename="tasks.log",
                    format="[%(asctime)s] %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    encoding="utf-8")

logger = logging.getLogger("tasks")


def logging_result(result: bool, 
                   id: Optional[str] = None, 
                   name_source: Optional[str] = None,
                   error_line: Optional[int] = None, 
                   error_text: Optional[str] = None):
    
    if result:
        logger.info(f"Задача {id} успешно обработана")
    else:
        all_error = ""

        if not (name_source is None):
            all_error += f"{name_source}: "

        if not (error_line is None):
            all_error += f"в строке {error_line}: "

        all_error += f"{error_text}"

        logger.error(all_error)