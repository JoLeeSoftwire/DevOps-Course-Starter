import pymongo
import os
from datetime import datetime
from bson.objectid import ObjectId
from .Task import Task, Status

class DbCommunicator:
    MONGODB_STRING = os.environ.get('MONGODB_STRING')
    client = pymongo.MongoClient(MONGODB_STRING)
    db = client.todo_app_db

    dateformat = "%Y-%m-%dT%H:%M:%S.%fZ"

    @classmethod
    def get_items(cls):
        """
        Fetches all saved items from the database.

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
        Adds a new item with the specified title and description to the ToDo collection in the database.

        Args:
            title: The title of the item.
            description: The description of the item.

        Returns:
            item: The saved item.
        """
        todos = cls.db.ToDo
        timestamp = datetime.now().strftime(cls.dateformat)
        document = {
            "name": title,
            "dateLastActivity": timestamp,
        }
        if description != None:
            document.update({"desc": description})
        
        taskId = todos.insert_one(document).inserted_id

        return Task(taskId, title, description=description, last_modified=timestamp)


    @classmethod
    def mark_done(cls, task_id):
        """
        Moves an existing document from 'ToDo' to 'Done' in the database. If no existing item matches the ID of the specified item, nothing is saved, and the page refreshes.

        Args:
            task_id: The id of the item to mark as done.
        """
        try:
            mongoDoc = cls.db.ToDo.find_one({"_id": ObjectId(task_id)})
            mongoDoc["dateLastActivity"] = datetime.now().strftime(cls.dateformat)
            cls.db.Done.insert_one(mongoDoc)
            cls.db.ToDo.delete_one({"_id": ObjectId(task_id)})
        except:
            print(f"card with id {str(task_id)} not found, will refresh")


    @classmethod
    def create_db(cls, name):
        test_db = DbCommunicator.client[name]
        return test_db

    @classmethod
    def delete_db(cls, name):
        # drop all the collections in that db, which is equivalent, since we don't have permission to drop dbs
        db = DbCommunicator.client[name]
        db.ToDo.drop()
        db.Done.drop()
        db.Doing.drop()
        return DbCommunicator.db
    