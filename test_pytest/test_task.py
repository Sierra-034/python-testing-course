import pytest
from datetime import datetime, timedelta

from mypytest import Task, DueDateError

class TestTask:
    def test_task(self):
        assert True
    
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'samuel_g', due_date)

        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'samuel_g'
        assert task.due_date == due_date

    @pytest.mark.due_date
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            task = Task('Title', 'Description', 'samuel_g', due_date)
    
    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'samuel_g', due_date)

        assert task.due_date > datetime.now()
