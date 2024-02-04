import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_addition(client):
    response = client.get('/add?a=3&b=4')
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert data['result'] == 7.0


def test_subtraction(client):
    response = client.get('/subtract?a=10&b=5')
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert data['result'] == 5.0


def test_multiplication(client):
    response = client.get('/multiply?a=2&b=8')
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert data['result'] == 16.0


def test_division(client):
    response = client.get('/divide?a=15&b=3')
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert data['result'] == 5.0


def test_division_by_zero(client):
    response = client.get('/divide?a=5&b=0')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == "Cannot divide by zero"
