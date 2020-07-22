import pytest
from datetime import datetime, timedelta
from todolist.ViewModel import ViewModel
from todolist.Task import Task, Status

dateformat = "%Y-%m-%dT%H:%M:%S.%fZ"

def test_show_all_done_if_less_than_five():
    # Given
    expectedDone = [
        Task(1, 'I did this', status=Status.Done),
        Task(2, "I did this too", status=Status.Done),
        Task(3, "another thing I did", status=Status.Done),
        Task(4, "oh and another thing", status=Status.Done),
        Task(5, "a fifth thing I have doned", status=Status.Done, last_modified=datetime.strptime("2020-06-29T09:17:20.141163Z", dateformat))
    ]
    inputTasks = {
        Status.ToDo: [],
        Status.Done: expectedDone,
        Status.Doing: []
    }

    # When
    vm = ViewModel(inputTasks)

    # Then
    assert vm.tasks[Status.Done] == expectedDone

### TODO: rewrite these to not fail for the first 2 hours of the day
def test_show_today_if_more_than_five_and_toggle_off():
    # Given
    task1DoneAt = datetime.now() - timedelta(minutes=15)
    task2DoneAt = datetime.now() - timedelta(minutes=10)
    task3DoneAt = datetime.strptime("2020-01-08T08:15:27.243860Z", dateformat)
    task4DoneAt = datetime.strptime("2020-06-29T09:17:20.141163Z", dateformat)
    task5DoneAt = datetime.now() - timedelta(minutes=1)
    task6DoneAt = datetime.now() - timedelta(minutes=120)
    expectedDone = [
        Task(1, 'I did this', status=Status.Done, last_modified=task1DoneAt),
        Task(2, "I did this too", status=Status.Done, last_modified=task2DoneAt),
        Task(5, "a fifth thing I have doned", status=Status.Done, last_modified=task5DoneAt),
        Task(6, "I did something else too", status=Status.Done, last_modified=task6DoneAt)
    ]
    inputTasks = {
        Status.ToDo: [],
        Status.Done: [
            Task(1, 'I did this', status=Status.Done, last_modified=task1DoneAt),
            Task(2, "I did this too", status=Status.Done, last_modified=task2DoneAt),
            Task(3, "another thing I did", status=Status.Done, last_modified=task3DoneAt),
            Task(4, "oh and another thing", status=Status.Done, last_modified=task4DoneAt),
            Task(5, "a fifth thing I have doned", status=Status.Done, last_modified=task5DoneAt),
            Task(6, "I did something else too", status=Status.Done, last_modified=task6DoneAt)
        ],
        Status.Doing: []
    }

    # When
    vm = ViewModel(inputTasks)

    # Then
    assert vm.tasks[Status.Done] == expectedDone

# def test_show_all_if_more_than-five_and_toggle_on

# def test_toggle_defaults_off

# def test_can_toggle_show_all