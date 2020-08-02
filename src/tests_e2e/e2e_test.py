import os
import pytest
from selenium import webdriver
from threading import Thread
from todolist.TrelloApi import TrelloApi
import todolist.app as app
from dotenv import find_dotenv, load_dotenv

@pytest.fixture(scope='module')
def test_app():
    # set up real api
    file_path = find_dotenv('.env.e2e_test')
    load_dotenv(file_path, override=True)

    trello_key = os.environ.get("TRELLO_KEY")
    trello_token = os.environ.get("TRELLO_TOKEN")
    TrelloApi.TRELLO_KEY = trello_key
    TrelloApi.TRELLO_TOKEN = trello_token
    TrelloApi.default_query_params = {
        'key': trello_key,
        'token': trello_token,
    }

    # Create the new board & update the board id environment variable
    board_id = TrelloApi.create_board("Test ToDo")["id"]
    TrelloApi.BOARD_ID = board_id
    
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

    test_task_name = "a test task"
    test_task_description = "with description"

    title_input = driver.find_element_by_name("title")
    title_input.send_keys(test_task_name)
    description_input = driver.find_element_by_name("description")
    description_input.send_keys(test_task_description)
    submit_button = driver.find_element_by_id("create_task")
    submit_button.click()

    # if there isn't exactly 1 entry, these will error
    checkbox = driver.find_element_by_class_name("checkbox")
    title = driver.find_element_by_class_name("task-title")
    description = driver.find_element_by_class_name("task-description")
    
    assert title.text == test_task_name
    assert description.text == ": " + test_task_description
