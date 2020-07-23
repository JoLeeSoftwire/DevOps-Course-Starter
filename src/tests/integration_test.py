import pytest
import requests
import todolist.app as app
from dotenv import find_dotenv, load_dotenv
from .fixtures import MockReturn

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    # Create the new app.
    test_app = app.create_app()
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):    
    monkeypatch.setattr(requests, "get", lambda endpoint, params: MockReturn(endpoint, params))
    response = client.get('/')
