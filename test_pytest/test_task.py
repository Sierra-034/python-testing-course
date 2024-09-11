import pytest
from datetime import datetime

from mypytest import Task

class TestTask:
    def test_task(self):
        assert True
    
    def test_new_task(self):
        due_date = datetime.now()
        task = Task('Title', 'Description', 'samuel_g', due_date)

        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'samuel_g'
        assert task.due_date == due_date
