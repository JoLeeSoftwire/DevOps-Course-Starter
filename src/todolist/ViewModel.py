from .Task import Task, Status

class ViewModel:
    def __init__(self, tasks):
        self._tasks = tasks
        self._show_all_done_items = False

    @property
    def tasks(self):
        return {
            "ToDo": self._tasks[Status.ToDo],
            "Doing": self._tasks[Status.Doing],
            "Done": {
                "recent": self.recent_done_items,
                "old": self.older_done_items
            }
        }

    @property
    def recent_done_items(self):
        return list(filter(lambda t:t.touchedToday(), self._tasks[Status.Done]))

    @property
    def older_done_items(self):
        return list(filter(lambda t:not t.touchedToday(), self._tasks[Status.Done]))