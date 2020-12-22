from todolist.Task import Task, Status
from datetime import datetime

dateformat = "%Y-%m-%dT%H:%M:%S.%fZ"

def test_created_on():
    # Given
    task1DoneAt = datetime.strptime("2020-12-22T00:00:00.000000Z", dateformat) # 22/12/2020
    task2DoneAt = datetime.strptime("2020-12-22T08:15:27.243860Z", dateformat) # 22/12/2020
    task3DoneAt = datetime.strptime("2020-01-08T08:15:27.243860Z", dateformat) # 08/01/2020
    task4DoneAt = datetime.strptime("2019-06-29T09:17:20.141163Z", dateformat) # 29/06/2019
    task5DoneAt = datetime.strptime("2020-12-22T08:12:01.243860Z", dateformat) # 22/12/2020
    task6DoneAt = datetime.strptime("2020-12-22T08:15:27.243860Z", dateformat) # 22/12/2020

    task1 = Task(1, 'I did this', status=Status.Done, last_modified=task1DoneAt)
    task2 = Task(2, "I did this too", status=Status.Done, last_modified=task2DoneAt)
    task3 = Task(3, "another thing I did", status=Status.Done, last_modified=task3DoneAt)
    task4 = Task(4, "oh and another thing", status=Status.Done, last_modified=task4DoneAt)
    task5 = Task(5, "a fifth thing I have doned", status=Status.Done, last_modified=task5DoneAt)
    task6 = Task(6, "I did something else too", status=Status.Done, last_modified=task6DoneAt)

    today = datetime.strptime("2020-12-22T12:34:56.789012Z", dateformat).date()

    # When
    task1touchedToday = task1.touchedOn(today)
    task2touchedToday = task2.touchedOn(today)
    task3touchedToday = task3.touchedOn(today)
    task4touchedToday = task4.touchedOn(today)
    task5touchedToday = task5.touchedOn(today)
    task6touchedToday = task6.touchedOn(today)

    # Then
    assert task1touchedToday == True
    assert task2touchedToday == True
    assert task3touchedToday == False
    assert task4touchedToday == False
    assert task5touchedToday == True
    assert task6touchedToday == True
