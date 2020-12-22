import pytest
from datetime import datetime, timedelta
from todolist.ViewModel import ViewModel
from todolist.Task import Task, Status

dateformat = "%Y-%m-%dT%H:%M:%S.%fZ"
dummyNotToday = datetime.strptime("2020-02-18T08:15:27.243860Z", dateformat)
dummyToday = datetime.strptime("2020-06-14T09:17:20.141163Z", dateformat)

### TODO: rewrite these to not fail for the first 2 hours of the day
def test_correct_recent_done_items(monkeypatch):
    # Given
    monkeypatch.setattr(Task, "touchedOn", lambda self, date: self.last_modified == dummyToday)

    expectedRecent = [
        Task(1, 'I did this', status=Status.Done, last_modified=dummyToday),
        Task(2, "I did this too", status=Status.Done, last_modified=dummyToday),
        Task(5, "a fifth thing I have doned", status=Status.Done, last_modified=dummyToday),
        Task(6, "I did something else too", status=Status.Done, last_modified=dummyToday)
    ]
    inputTasks = {
        Status.ToDo: [],
        Status.Done: [
            Task(1, 'I did this', status=Status.Done, last_modified=dummyToday),
            Task(2, "I did this too", status=Status.Done, last_modified=dummyToday),
            Task(3, "another thing I did", status=Status.Done, last_modified=dummyNotToday),
            Task(4, "oh and another thing", status=Status.Done, last_modified=dummyNotToday),
            Task(5, "a fifth thing I have doned", status=Status.Done, last_modified=dummyToday),
            Task(6, "I did something else too", status=Status.Done, last_modified=dummyToday)
        ],
        Status.Doing: []
    }

    # When
    vm = ViewModel(inputTasks)

    # Then
    assert vm.recent_done_items == expectedRecent

def test_show_all_if_more_than_five_and_toggle_on(monkeypatch):
    # Given
    monkeypatch.setattr(Task, "touchedOn", lambda self, date: self.last_modified == dummyToday)

    expectedOld = [
        Task(3, "another thing I did", status=Status.Done, last_modified=dummyNotToday),
        Task(4, "oh and another thing", status=Status.Done, last_modified=dummyNotToday)
    ]
    inputTasks = {
        Status.ToDo: [],
        Status.Done: [
            Task(1, 'I did this', status=Status.Done, last_modified=dummyToday),
            Task(2, "I did this too", status=Status.Done, last_modified=dummyToday),
            Task(3, "another thing I did", status=Status.Done, last_modified=dummyNotToday),
            Task(4, "oh and another thing", status=Status.Done, last_modified=dummyNotToday),
            Task(5, "a fifth thing I have doned", status=Status.Done, last_modified=dummyToday),
            Task(6, "I did something else too", status=Status.Done, last_modified=dummyToday)
        ],
        Status.Doing: []
    }

    # When
    vm = ViewModel(inputTasks)

    # Then
    assert vm.older_done_items == expectedOld