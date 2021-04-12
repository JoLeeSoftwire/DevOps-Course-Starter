import enum
from datetime import datetime

class Status(enum.Enum):
    ToDo = 0
    Done = 1
    Doing = 2

class Task:

    def __init__(self, id, title, status=Status.ToDo, description=None, last_modified=datetime.now()):
        self.id = id
        self.title = title
        self.status = status
        self.description = description
        self.last_modified = last_modified

    @classmethod
    def from_mongo(cls, item, status=Status.ToDo):
        dateformat = "%Y-%m-%dT%H:%M:%S.%fZ"
        
        task = cls.__new__(cls)
        task.id = item['_id']
        task.title = item['name']
        task.status = status
        task.description = item['desc']
        task.last_modified = datetime.strptime(item['dateLastActivity'], dateformat)
        return task

    def touchedToday(self):
        return self.last_modified.date() == datetime.now().date()

    def prettyPrint(self):
        print('{')
        print('\tid: '+self.id+',')
        print('\ttitle: '+self.title+',')
        print('\tstatus: '+self.status.name+',')
        if(self.description != None):
            print('\tdescription: '+self.description)
        print('\tlast modified: '+self.last_modified)
        print('}')

    def __str__(self):
        return 'Task(id='+self.id+')'

    def __eq__(self, other):
        if not isinstance(other, Task):
            # don't attempt to compare against unrelated types
            return NotImplemented

        idMatch = self.id == other.id
        titleMatch = self.title == other.title
        statusMatch = self.status == other.status
        descriptionMatch = self.description == other.description

        return idMatch and titleMatch and statusMatch and descriptionMatch