from datetime import date, timedelta

class Chore:
    def __init__(self, name, assigned_to, interval_days, initial_due_date=None):
        self.name = name
        self.assigned_to = assigned_to
        self.interval_days = interval_days
        self.next_due = initial_due_date or date.today()

    def complete(self, completed_date=None):
        completed_date = completed_date or date.today()
        self.next_due = completed_date + timedelta(days=self.interval_days)

    def __repr__(self):
        return f"{self.name} (Assigned to: {self.assigned_to}, Next Due: {self.next_due})"

class DailyChoresSensor:
    def __init__(self, name):
        self._name = name
        self._state = None
        self._chores = []

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        if self._chores:
            self._state = "Chores Pending"
        else:
            self._state = "All Chores Completed"

    def add_chore(self, name, assigned_to, interval_days, initial_due_date=None):
        chore = Chore(name, assigned_to, interval_days, initial_due_date)
        self._chores.append(chore)
        self.update()

    def complete_chore(self, name, completed_date=None):
        for chore in self._chores:
            if chore.name == name:
                chore.complete(completed_date)
                break
        self.update()

    def get_chores(self):
        return self._chores.copy()