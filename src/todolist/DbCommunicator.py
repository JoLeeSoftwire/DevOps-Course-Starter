import pymongo
import os

from .Task import Task, Status

class DbCommunicator:
    MONGODB_STRING = os.environ.get('MONGODB_STRING')
    client = pymongo.MongoClient(MONGODB_STRING)
    db = client.todo_app_db

    @classmethod
    def get_items(cls):
        """
        Fetches all saved items from Trello.

        Returns:
            list: The list of saved items.
        """
        
        todo = DbCommunicator.get_items_with_status(Status.ToDo)
        done = DbCommunicator.get_items_with_status(Status.Done)
        doing = DbCommunicator.get_items_with_status(Status.Doing)

        return {
            Status.ToDo: todo,
            Status.Doing: doing,
            Status.Done: done
        }

    @classmethod
    def get_items_with_status(cls, status):
        mongoTasks = cls.db[status.name].find()
        tasks = list()
        for item in mongoTasks:
            taskObj = Task.from_mongo(item, status)
            tasks.append(taskObj)
        
        return tasks

    @classmethod
    def add_item(cls, title, description=None):
        """
        Adds a new item with the specified title and description to the ToDo list in Trello.

        Args:
            title: The title of the item.
            description: The description of the item.

        Returns:
            item: The saved item.
        """
        todos = db.ToDo
        document = {
            "name": title,
            'idList': listIds[Status.ToDo],
        }
        if description != None:
            document.update({"desc": description})
        
        taskId = todos.insert_one(document).inserted_id

        return Task(taskId, title, description=description)

