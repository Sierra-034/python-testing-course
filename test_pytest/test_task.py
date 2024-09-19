import pytest
from datetime import datetime, timedelta

from mypytest import Task, DueDateError

@pytest.fixture
def username():
    print('\n>>> Antes de prueba')
    yield 'Cody'
    print('\n>>> Depués de prueba')

@pytest.fixture
def password():
    return 'password'

def test_username(username):
    assert username == 'Cody'

def test_username_and_password(username, password):
    assert username == 'Cody'
    assert password == 'password'

def is_available_to_skip():
    return True

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
    
    @pytest.mark.skipif(is_available_to_skip(), reason='La prueba no cumple los requerimientos.')
    def test_skip(self):
        pass
