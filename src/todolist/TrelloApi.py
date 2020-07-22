import os
import requests

from .Task import Task, Status

BOARD_ID = os.environ.get('BOARD_ID')
TRELLO_KEY = os.environ.get("TRELLO_KEY")
TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")

trello_baseurl = "https://api.trello.com/"
trello_apiversion = '1'
trello_commonurl = trello_baseurl + trello_apiversion
boardselector = "/board/"
listselector = "/lists/"
cardselector = "/cards/"

default_query_params = {
    'key': TRELLO_KEY,
    'token': TRELLO_TOKEN,
}

class TrelloApi:
    @staticmethod
    def get_items():
        """
        Fetches all saved items from Trello.

        Returns:
            list: The list of saved items.
        """
        
        todo = TrelloApi.get_items_with_status(Status.ToDo)
        done = TrelloApi.get_items_with_status(Status.Done)

        return {
            Status.ToDo: todo,
            Status.Done: done
        }

    @staticmethod
    def get_items_with_status(status):
        listIds = TrelloApi.get_list_ids()
        statusId = listIds[status]
        endpoint = trello_commonurl + listselector + statusId + cardselector
        trelloTasks = requests.get(endpoint, params=default_query_params).json()

        tasks = list()
        for item in trelloTasks:
            taskObj = Task.from_trello(item, status)
            tasks.append(taskObj)
        
        return tasks


    @staticmethod
    def add_item(title, description=None):
        """
        Adds a new item with the specified title and description to the ToDo list in Trello.

        Args:
            title: The title of the item.
            description: The description of the item.

        Returns:
            item: The saved item.
        """
        endpoint = trello_commonurl + cardselector
        listIds = TrelloApi.get_list_ids()
        extraparams = {
            "name": title,
            'idList': listIds[Status.ToDo]
        }
        if description != None:
            extraparams.update({"desc": description})
            
        allparams = TrelloApi.custom_query_params(extraparams)

        trelloTodo = requests.post(endpoint, params=allparams).json()

        return Task(trelloTodo['id'], title, description=description)


    @staticmethod
    def mark_done(task_id):
        """
        Updates an existing item in Trello. If no existing item matches the ID of the specified item, nothing is saved, and the page refreshes.

        Args:
            task_id: The id of the item to mark as done.
        """
        endpoint = trello_commonurl + cardselector + task_id
        listIds = TrelloApi.get_list_ids()
        extraparams = {
            "idList": listIds[Status.Done]
        }
        allparams = TrelloApi.custom_query_params(extraparams)

        try:
            trelloDone = requests.put(endpoint, params=allparams).json()
        except:
            print(f"card with id {str(id)} not found, will refresh")

    @staticmethod
    def custom_query_params(params):
        newDictionary = {**default_query_params, **params} 
        return newDictionary

    @staticmethod
    def get_list_ids():
        endpoint = trello_commonurl + boardselector + BOARD_ID + listselector
        try:
            trelloLists = requests.get(endpoint, params=default_query_params).json()
        except:
            print(f"board with id {BOARD_ID} not found, check config")
        
        listIds = {
            Status.ToDo: "no ToDo list found for this board",
            Status.Done: "no Done list found for this board"
        }
        for list in trelloLists:
            if(list["name"] == "To Do"):
                listIds[Status.ToDo] = list["id"]
            if(list["name"] == "Done"):
                listIds[Status.Done] = list["id"]
        return listIds