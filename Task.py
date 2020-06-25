import enum

class Status(enum.Enum):
    ToDo = 0
    Done = 1
    # Doing = 2

class Task:

    def __init__(self, id, title, status=Status.ToDo):
        self.id = id
        self.title = title
        self.status = status
