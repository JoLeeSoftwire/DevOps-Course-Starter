import enum

class Status(enum.Enum):
    ToDo = 0
    Done = 1
    # Doing = 2

class Task:

    def __init__(self, id, title, status=Status.ToDo, description=None):
        self.id = id
        self.title = title
        self.status = status
        self.description = description

    @classmethod
    def from_trello(cls, item, status=Status.ToDo):
        task = cls.__new__(cls)
        task.id = item['id']
        task.title = item['name']
        task.status = status
        task.description = item['desc']
        return task
