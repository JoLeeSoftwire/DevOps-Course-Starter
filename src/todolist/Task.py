import enum

class Status(enum.Enum):
    ToDo = 0
    Done = 1
    Doing = 2

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

    def prettyPrint(self):
        print('{')
        print('\tid: '+self.id+',')
        print('\ttitle: '+self.title+',')
        print('\tstatus: '+self.status.name+',')
        if(self.description != None):
            print('\tdescription: '+self.description)
        print('}')

    def __eq__(self, other):
        if not isinstance(other, Task):
            # don't attempt to compare against unrelated types
            return NotImplemented

        idMatch = self.id == other.id
        titleMatch = self.title == other.title
        statusMatch = self.status == other.status
        descriptionMatch = self.description == other.description

        return idMatch and titleMatch and statusMatch and descriptionMatch