import os
import pytest
import requests
import pymongo
from todolist.DbCommunicator import DbCommunicator
from todolist.Task import Task, Status
from unittest import mock

def test_get_todo_items(monkeypatch):
    # Given
    todo_docs = [
            {
                "_id": "5ef487407c6915497a7610a3",
                "dateLastActivity": "2020-06-25T11:15:12.453Z",
                "desc": "",
                "name": "make it give a sensible message if a card is deleted",
            },
            {
                "_id": "5ef48d1e29fc363139d1b134",
                "dateLastActivity": "2020-06-25T11:40:14.718Z",
                "desc": "and some testing?",
                "name": "ame release",
            },
            {
                "_id": "5ef48d2ac2352a2856c43c76",
                "dateLastActivity": "2020-06-25T11:40:26.170Z",
                "desc": "",
                "name": "task with no desc",
            }
        ]
    db_mock = {
        "ToDo": mock.Mock(),
    }
    db_mock['ToDo'].find.return_value = todo_docs
    DbCommunicator.db = db_mock

    expectedToDos = [
        Task("5ef487407c6915497a7610a3", "make it give a sensible message if a card is deleted", status=Status.ToDo, description="" ),
        Task("5ef48d1e29fc363139d1b134", "ame release", status=Status.ToDo, description="and some testing?"),
        Task("5ef48d2ac2352a2856c43c76", "task with no desc", status=Status.ToDo, description="")
    ]

    # When
    todos = DbCommunicator.get_items_with_status(Status.ToDo)

    # Then
    assert expectedToDos == todos

# def test_get_done_items(monkeypatch):
#     # Given
#     monkeypatch.setattr(TrelloApi, "get_list_ids", lambda: {Status.ToDo: '1', Status.Done: '2'})
    
#     monkeypatch.setattr(requests, "get", lambda endpoint, params: MockReturn(endpoint, params))
#     expectedDone = [
#         Task("2ef487407c6915497a7610a3", "test card", status=Status.Done, description="" ),
#         Task("2ef48d1e29fc363139d1b134", "another task", status=Status.Done, description="with a description"),
#     ]

#     # When
#     done = TrelloApi.get_items_with_status(Status.Done)

#     # Then
#     assert expectedDone == done

# def test_get_doing_items(monkeypatch):
#     # Given
#     monkeypatch.setattr(TrelloApi, "get_list_ids", lambda: {Status.ToDo: '1', Status.Done: '2', Status.Doing: '3'})
    
#     monkeypatch.setattr(requests, "get", lambda endpoint, params: MockReturn(endpoint, params))
#     expectedDoing = [
#         Task("3ef487407c6915497a7610a3", "I'll finish it later", status=Status.Doing, description="eventually" ),
#         Task("3ef48d1e29fc363139d1b134", "half way through this", status=Status.Doing, description=""),
#     ]

#     # When
#     doing = TrelloApi.get_items_with_status(Status.Doing)

#     # Then
#     assert expectedDoing == doing