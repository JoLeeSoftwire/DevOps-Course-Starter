import pytest
from datetime import datetime
from todolist.ViewModel import ViewModel
from todolist.Task import Task, Status

dateformat = "%Y-%m-%dT%H:%M:%S.%fZ"

### TODO: rewrite these to not fail for the first 2 hours of the day
def test_correct_recent_done_items():
    # Given
    task1DoneAt = datetime.now().replace(minute=13, hour=1)
    task2DoneAt = datetime.now().replace(minute=0, hour=9)
    task3DoneAt = datetime.strptime("2020-01-08T08:15:27.243860Z", dateformat)
    task4DoneAt = datetime.strptime("2020-06-29T09:17:20.141163Z", dateformat)
    task5DoneAt = datetime.now().replace(minute=59, hour=23)
    task6DoneAt = datetime.now().replace(minute=45, hour=5)
    expectedRecent = [
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
    vm = ViewModel(inputTasks, True)

    # Then
    assert vm.recent_done_items == expectedRecent

def test_show_all_if_more_than_five_and_toggle_on():
    # Given
    task1DoneAt = datetime.now().replace(minute=13, hour=1)
    task2DoneAt = datetime.now().replace(minute=0, hour=9)
    task3DoneAt = datetime.strptime("2020-01-08T08:15:27.243860Z", dateformat)
    task4DoneAt = datetime.strptime("2020-06-29T09:17:20.141163Z", dateformat)
    task5DoneAt = datetime.now().replace(minute=59, hour=23)
    task6DoneAt = datetime.now().replace(minute=45, hour=5)
    expectedOld = [
        Task(3, "another thing I did", status=Status.Done, last_modified=task3DoneAt),
        Task(4, "oh and another thing", status=Status.Done, last_modified=task4DoneAt)
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
    vm = ViewModel(inputTasks, True)

    # Then
    assert vm.older_done_items == expectedOld