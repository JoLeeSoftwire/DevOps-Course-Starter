class ViewModel:
    def __init__(self, tasks):
        self._tasks = tasks
        self._show_all_done_items = False

    @property
    def tasks(self):
        return self._tasks