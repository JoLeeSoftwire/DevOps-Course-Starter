import pymongo
import os

from .Task import Task, Status

class DbCommunicator:
    MONGODB_STRING = os.environ.get('MONGODB_STRING')
    client = pymongo.MongoClient(MONGODB_STRING)
    db = client.todo_app_db

    @classmethod
    def get_items_with_status(cls, status):
        mongoTasks = cls.db[status.name].find()
        tasks = list()
        for item in mongoTasks:
            taskObj = Task.from_mongo(item, status)
            tasks.append(taskObj)
        
        return tasks

    