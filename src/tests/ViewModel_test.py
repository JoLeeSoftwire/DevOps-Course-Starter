import pytest
import datetime
from todolist.ViewModel import ViewModel
from todolist.Task import Task, Status

def test_show_all_done_if_less_than_five(monkeypatch):
    # Given
    expectedDone = [
        Task(1, 'I did this', Status.Done),
        Task(2, "I did this too", Status.Done),
        Task(3, "another thing I did", Status.Done),
        Task(4, "oh and another thing", Status.Done),
        Task(5, "a fifth thing I have doned", Status.Done)
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

# def test_show_today_if_more_than_five_and_toggle_off

# def test_show_all_if_more_than-five_and_toggle_on

# def test_toggle_defaults_off

# def test_can_toggle_show_all