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
