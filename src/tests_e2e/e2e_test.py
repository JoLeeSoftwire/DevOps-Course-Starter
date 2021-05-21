import os
import pytest
from selenium import webdriver
from threading import Thread
from todolist.DbCommunicator import DbCommunicator
import todolist.app as app
from dotenv import find_dotenv, load_dotenv
from tests.AnonUser import AnonUser

@pytest.fixture(scope='module')
def test_app():
    # Create the test db & update the db in DbCommunicator
    test_db = DbCommunicator.create_db("test-todo")
    DbCommunicator.db = test_db
    
    # construct the new application
    application = app.create_app()
    application.config['LOGIN_DISABLED']=True
    application.login_manager.anonymous_user = AnonUser
    
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    
    # Tear Down
    thread.join(1)
    DbCommunicator.delete_db("test-todo")
    # DbCommunicator.db = DbCommunicator.client.todo_app_db


@pytest.fixture(scope="module")
def driver():
    opts = webdriver.ChromeOptions()
    # opts.add_argument('--headless')
    # opts.add_argument('--no-sandbox')
    # opts.add_argument('--disable-dev-shm-usage')
    # with webdriver.Chrome('./chromedriver', options=opts) as driver:
    # use the below for running locally, or above for running in a docker container
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

    # if there isn't exactly 1 entry (and it has a checkbox), these will error
    checkbox = driver.find_element_by_class_name("checkbox")
    todo_title = driver.find_element_by_class_name("task-title")
    todo_description = driver.find_element_by_class_name("task-description")
    
    assert todo_title.text == test_task_name
    assert todo_description.text == ": " + test_task_description

    checkbox.click()

    # if there isn't exactly 1 entry (and it has a checkmark), these will error
    checkmark = driver.find_element_by_class_name("checkmark")
    done_title = driver.find_element_by_class_name("task-title")
    done_description = driver.find_element_by_class_name("task-description")

    assert done_title.text == test_task_name
    assert done_description.text == ": " + test_task_description
