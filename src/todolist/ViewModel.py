from .Task import Task, Status

class ViewModel:
    def __init__(self, tasks, show_all_done_items=False):
        self._tasks = tasks
        self._show_all_done_items = show_all_done_items

    @property
    def tasks(self):
        tasks_to_show = self.recent_done_items
        return {
            Status.ToDo: self._tasks[Status.ToDo],
            Status.Doing: self._tasks[Status.Doing],
            Status.Done: tasks_to_show
        }

    @property
    def recent_done_items(self):
        if(len(self._tasks[Status.Done]) <= 5):
            return self._tasks[Status.Done]
        return list(filter(lambda t:t.touchedToday(), self._tasks[Status.Done]))