# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b"Items" in rv.data

def test_add_item(client):
    rv = client.post('/add', data=dict(item="Test item"), follow_redirects=True)
    assert b"Test item" in rv.data