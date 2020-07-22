import pytest
import requests
from todolist.TrelloApi import TrelloApi
from todolist.Task import Task, Status

class MockReturn:
    def __init__(self, endpoint, params):
        self.endpoint = endpoint
        self.params = params

    def json(self):
        todos = [
            {
                "id": "5ef487407c6915497a7610a3",
                "checkItemStates": None,
                "closed": False,
                "dateLastActivity": "2020-06-25T11:15:12.453Z",
                "desc": "",
                "descData": None,
                "dueReminder": None,
                "idBoard": "5eecd4bae16d0019c3f56345",
                "idList": "5eecd4bae16d0019c3f56346",
                "idMembersVoted": [],
                "idShort": 10,
                "idAttachmentCover": None,
                "idLabels": [],
                "manualCoverAttachment": False,
                "name": "make it give a sensible message if a card is deleted",
                "pos": 147455,
                "shortLink": "AGKOOyA5",
                "isTemplate": False,
                "badges": {
                    "attachmentsByType": {
                        "trello": {
                            "board": 0,
                            "card": 0
                        }
                    },
                    "location": False,
                    "votes": 0,
                    "viewingMemberVoted": False,
                    "subscribed": False,
                    "fogbugz": "",
                    "checkItems": 0,
                    "checkItemsChecked": 0,
                    "checkItemsEarliestDue": None,
                    "comments": 0,
                    "attachments": 0,
                    "description": False,
                    "due": None,
                    "dueComplete": False
                },
                "dueComplete": False,
                "due": None,
                "idChecklists": [],
                "idMembers": [],
                "labels": [],
                "shortUrl": "https://trello.com/c/AGKOOyA5",
                "subscribed": False,
                "url": "https://trello.com/c/AGKOOyA5/10-make-it-give-a-sensible-message-if-a-card-is-deleted",
                "cover": {
                    "idAttachment": None,
                    "color": None,
                    "idUploadedBackground": None,
                    "size": "normal",
                    "brightness": "light"
                }
            },
            {
                "id": "5ef48d1e29fc363139d1b134",
                "checkItemStates": None,
                "closed": False,
                "dateLastActivity": "2020-06-25T11:40:14.718Z",
                "desc": "and some testing?",
                "descData": None,
                "dueReminder": None,
                "idBoard": "5eecd4bae16d0019c3f56345",
                "idList": "5eecd4bae16d0019c3f56346",
                "idMembersVoted": [],
                "idShort": 11,
                "idAttachmentCover": None,
                "idLabels": [],
                "manualCoverAttachment": False,
                "name": "ame release",
                "pos": 163839,
                "shortLink": "bf6HQUuk",
                "isTemplate": False,
                "badges": {
                    "attachmentsByType": {
                        "trello": {
                            "board": 0,
                            "card": 0
                        }
                    },
                    "location": False,
                    "votes": 0,
                    "viewingMemberVoted": False,
                    "subscribed": False,
                    "fogbugz": "",
                    "checkItems": 0,
                    "checkItemsChecked": 0,
                    "checkItemsEarliestDue": None,
                    "comments": 0,
                    "attachments": 0,
                    "description": True,
                    "due": None,
                    "dueComplete": False
                },
                "dueComplete": False,
                "due": None,
                "idChecklists": [],
                "idMembers": [],
                "labels": [],
                "shortUrl": "https://trello.com/c/bf6HQUuk",
                "subscribed": False,
                "url": "https://trello.com/c/bf6HQUuk/11-ame-release",
                "cover": {
                    "idAttachment": None,
                    "color": None,
                    "idUploadedBackground": None,
                    "size": "normal",
                    "brightness": "light"
                }
            },
            {
                "id": "5ef48d2ac2352a2856c43c76",
                "checkItemStates": None,
                "closed": False,
                "dateLastActivity": "2020-06-25T11:40:26.170Z",
                "desc": "",
                "descData": None,
                "dueReminder": None,
                "idBoard": "5eecd4bae16d0019c3f56345",
                "idList": "5eecd4bae16d0019c3f56346",
                "idMembersVoted": [],
                "idShort": 12,
                "idAttachmentCover": None,
                "idLabels": [],
                "manualCoverAttachment": False,
                "name": "task with no desc",
                "pos": 180223,
                "shortLink": "HUPvAbEJ",
                "isTemplate": False,
                "badges": {
                    "attachmentsByType": {
                        "trello": {
                            "board": 0,
                            "card": 0
                        }
                    },
                    "location": False,
                    "votes": 0,
                    "viewingMemberVoted": False,
                    "subscribed": False,
                    "fogbugz": "",
                    "checkItems": 0,
                    "checkItemsChecked": 0,
                    "checkItemsEarliestDue": None,
                    "comments": 0,
                    "attachments": 0,
                    "description": False,
                    "due": None,
                    "dueComplete": False
                },
                "dueComplete": False,
                "due": None,
                "idChecklists": [],
                "idMembers": [],
                "labels": [],
                "shortUrl": "https://trello.com/c/HUPvAbEJ",
                "subscribed": False,
                "url": "https://trello.com/c/HUPvAbEJ/12-task-with-no-desc",
                "cover": {
                    "idAttachment": None,
                    "color": None,
                    "idUploadedBackground": None,
                    "size": "normal",
                    "brightness": "light"
                }
            }
        ]
        done = [
            {
                "id": "2ef487407c6915497a7610a3",
                "checkItemStates": None,
                "closed": False,
                "dateLastActivity": "2020-06-25T11:15:12.453Z",
                "desc": "",
                "descData": None,
                "dueReminder": None,
                "idBoard": "5eecd4bae16d0019c3f56345",
                "idList": "5eecd4bae16d0019c3f56348",
                "idMembersVoted": [],
                "idShort": 10,
                "idAttachmentCover": None,
                "idLabels": [],
                "manualCoverAttachment": False,
                "name": "test card",
                "pos": 147455,
                "shortLink": "AGKOOyA5",
                "isTemplate": False,
                "badges": {
                    "attachmentsByType": {
                        "trello": {
                            "board": 0,
                            "card": 0
                        }
                    },
                    "location": False,
                    "votes": 0,
                    "viewingMemberVoted": False,
                    "subscribed": False,
                    "fogbugz": "",
                    "checkItems": 0,
                    "checkItemsChecked": 0,
                    "checkItemsEarliestDue": None,
                    "comments": 0,
                    "attachments": 0,
                    "description": False,
                    "due": None,
                    "dueComplete": False
                },
                "dueComplete": False,
                "due": None,
                "idChecklists": [],
                "idMembers": [],
                "labels": [],
                "shortUrl": "https://trello.com/c/AGKOOyA5",
                "subscribed": False,
                "url": "https://trello.com/c/AGKOOyA5/10-make-it-give-a-sensible-message-if-a-card-is-deleted",
                "cover": {
                    "idAttachment": None,
                    "color": None,
                    "idUploadedBackground": None,
                    "size": "normal",
                    "brightness": "light"
                }
            },
            {
                "id": "2ef48d1e29fc363139d1b134",
                "checkItemStates": None,
                "closed": False,
                "dateLastActivity": "2020-06-25T11:40:14.718Z",
                "desc": "with a description",
                "descData": None,
                "dueReminder": None,
                "idBoard": "5eecd4bae16d0019c3f56345",
                "idList": "5eecd4bae16d0019c3f56348",
                "idMembersVoted": [],
                "idShort": 11,
                "idAttachmentCover": None,
                "idLabels": [],
                "manualCoverAttachment": False,
                "name": "another task",
                "pos": 163839,
                "shortLink": "bf6HQUuk",
                "isTemplate": False,
                "badges": {
                    "attachmentsByType": {
                        "trello": {
                            "board": 0,
                            "card": 0
                        }
                    },
                    "location": False,
                    "votes": 0,
                    "viewingMemberVoted": False,
                    "subscribed": False,
                    "fogbugz": "",
                    "checkItems": 0,
                    "checkItemsChecked": 0,
                    "checkItemsEarliestDue": None,
                    "comments": 0,
                    "attachments": 0,
                    "description": True,
                    "due": None,
                    "dueComplete": False
                },
                "dueComplete": False,
                "due": None,
                "idChecklists": [],
                "idMembers": [],
                "labels": [],
                "shortUrl": "https://trello.com/c/bf6HQUuk",
                "subscribed": False,
                "url": "https://trello.com/c/bf6HQUuk/11-ame-release",
                "cover": {
                    "idAttachment": None,
                    "color": None,
                    "idUploadedBackground": None,
                    "size": "normal",
                    "brightness": "light"
                }
            }
        ]
        if(self.endpoint == "https://api.trello.com/1/lists/1/cards/"):
            return todos
        if(self.endpoint == "https://api.trello.com/1/lists/2/cards/"):
            return done
        else:
            return []

def test_get_todo_items(monkeypatch):
    # Given
    monkeypatch.setattr(TrelloApi, "get_list_ids", lambda: {Status.ToDo: '1', Status.Done: '2'})
    
    monkeypatch.setattr(requests, "get", lambda endpoint, params: MockReturn(endpoint, params))
    expectedToDos = [
        Task("5ef487407c6915497a7610a3", "make it give a sensible message if a card is deleted", status=Status.ToDo, description="" ),
        Task("5ef48d1e29fc363139d1b134", "ame release", status=Status.ToDo, description="and some testing?"),
        Task("5ef48d2ac2352a2856c43c76", "task with no desc", status=Status.ToDo, description="")
    ]

    # When
    todos = TrelloApi.get_items_with_status(Status.ToDo)

    # Then
    assert expectedToDos == todos

def test_get_done_items(monkeypatch):
    # Given
    monkeypatch.setattr(TrelloApi, "get_list_ids", lambda: {Status.ToDo: '1', Status.Done: '2'})
    
    monkeypatch.setattr(requests, "get", lambda endpoint, params: MockReturn(endpoint, params))
    expectedDone = [
        Task("2ef487407c6915497a7610a3", "test card", status=Status.Done, description="" ),
        Task("2ef48d1e29fc363139d1b134", "another task", status=Status.Done, description="with a description"),
    ]

    # When
    done = TrelloApi.get_items_with_status(Status.Done)

    # Then
    assert expectedDone == done