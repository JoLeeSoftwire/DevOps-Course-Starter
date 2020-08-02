import pytest
import requests
import todolist.app as app
from todolist.TrelloApi import TrelloApi
from dotenv import find_dotenv, load_dotenv
from .fixtures import MockReturn
import os

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    TrelloApi.BOARD_ID = os.environ.get('BOARD_ID')
    
    # Create the new app.
    test_app = app.create_app()
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):    
    monkeypatch.setattr(requests, "get", lambda endpoint, params: MockReturn(endpoint, params))
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

