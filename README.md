# Лабораторная работа 2, семестр 2, python.

```
 git clone https://github.com/DariEFAL/sem-2-python-lab-1.git
 cd sem-2-python-lab-1
 uv venv
 source .venv/bin/activate
 (Для windows: .venv\Scripts\Activate.ps1)

 Установка зависимостей:
 uv pip install -e .

 Вызов тестов: 
 pytest tests -v

 Вызов программы: python -m main 
```

# Источники задач:
* jsonl: python -m main --jsonl *путь к файлу*
* stdin: python -m main --stdin
* genirator: python -m main --gen *кол-во задач, которые надо сгенерировать*

# Различие 1) Non-data descriptors и 2) data descriptors:
1) Не имеет метода __set__. Есть только метод __get__. Пример: метод age в классе Task
2) Есть __get__ и __set__. Пример любой дескриптор из папки descriptors

