from datetime import datetime

class DueDateError(Exception):
    pass

class Task:
    def __init__(self, title, description, assigned_to, due_date):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to

        if due_date < datetime.now():
            raise DueDateError('Invalid due date')
        
        self.due_date = due_date
