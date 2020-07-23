import os
import pytest
from selenium import webdriver
from threading import Thread
from todolist.TrelloApi import TrelloApi

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = TrelloApi.create_board("Test ToDo")["id"]
    os.environ['BOARD_ID'] = board_id
    
    # construct the new application
    application = app.create_app()
    
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    
    # Tear Down
    thread.join(1)
    TrelloApi.delete_board(board_id)

@pytest.fixture(scope="module")
def driver():
    with webdriver.Chrome() as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'