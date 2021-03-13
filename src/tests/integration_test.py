import pytest
import requests
import todolist.app as app
from todolist.DbCommunicator import DbCommunicator
from dotenv import find_dotenv, load_dotenv
import os
from unittest import mock

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    DbCommunicator.MONGODB_STRING = os.environ.get('MONGODB_STRING')
    
    # Create the new app.
    test_app = app.create_app()
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
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
    done_docs = [
            {
                "_id": "2ef487407c6915497a7610a3",
                "dateLastActivity": "2020-06-25T11:15:12.453Z",
                "desc": "",
                "name": "test card",
            },
            {
                "_id": "2ef48d1e29fc363139d1b134",
                "dateLastActivity": "2020-06-25T11:40:14.718Z",
                "desc": "with a description",
                "name": "another task",
            }
        ]
    doing_docs = [
            {
                "_id": "3ef487407c6915497a7610a3",
                "dateLastActivity": "2020-06-25T11:15:12.453Z",
                "desc": "eventually",
                "name": "I'll finish it later",
            },
            {
                "_id": "3ef48d1e29fc363139d1b134",
                "dateLastActivity": "2020-06-25T11:40:14.718Z",
                "desc": "",
                "name": "half way through this",
            }
        ]
    
    db_mock = {
        "ToDo": mock.Mock(),
        "Done": mock.Mock(),
        "Doing": mock.Mock()
    }
    db_mock['ToDo'].find.return_value = todo_docs
    db_mock['Done'].find.return_value = done_docs
    db_mock['Doing'].find.return_value = doing_docs
    DbCommunicator.db = db_mock

    response = client.get('/')
    content = response.data.decode('utf-8')
    print(content)
    assert "make it give a sensible message if a card is deleted" in content
    assert "ame release" in content
    assert "and some testing?" in content
    assert "task with no desc" in content
    assert "test card" in content
    assert "another task" in content
    assert "with a description" in content
    assert "I&#39;ll finish it later" in content
    assert "eventually" in content
    assert "half way through this" in content

