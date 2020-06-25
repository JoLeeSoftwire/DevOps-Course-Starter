from flask import session
import os
import requests

from Task import Task, Status

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

BOARD_ID = os.environ.get('BOARD_ID')
TRELLO_KEY = os.environ.get("TRELLO_KEY")
TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")

TODO_LIST_ID = os.environ.get("TODO_LIST_ID")
DONE_LIST_ID = os.environ.get("DONE_LIST_ID")

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

statusToID = {
    Status.ToDo: TODO_LIST_ID,
    Status.Done: DONE_LIST_ID
}
IDToStatus = {
    TODO_LIST_ID: Status.ToDo,
    DONE_LIST_ID: Status.Done
}

def get_items():
    """
    Fetches all saved items from Trello.

    Returns:
        list: The list of saved items.
    """
    
    todo = get_items_with_satus(Status.ToDo)
    done = get_items_with_satus(Status.Done)

    return todo + done

def get_items_with_satus(status):
    endpoint = trello_commonurl + listselector + statusToID[status] + cardselector
    trelloTasks = requests.get(endpoint, params=default_query_params).json()

    tasks = list()
    for item in trelloTasks:
        taskObj = Task(item['id'], item['name'], status)
        tasks.append(taskObj)
    
    return tasks


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    endpoint = trello_commonurl + cardselector + id
    trelloTask = requests.get(endpoint, params=default_query_params).json()
    
    return Task(trelloTask['id'], trelloTask['name'], IDToStatus[trelloTask['idList']])


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    endpoint = trello_commonurl + cardselector
    extra_params = {
        "name": title,
        "idList": TODO_LIST_ID
    }

    trelloTodo = requests.post(endpoint, params=custom_query_params(extra_params)).json()

    return Task(trelloTodo['id'], trelloTodo['name'], Status.ToDo)


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def custom_query_params(params):
    newDictionary = {**default_query_params, **params} 
    return newDictionary