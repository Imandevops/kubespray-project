import pytest
from authenticate.authenticate import create_app



@pytest.fixture
def app():
    app = create_app()
    return app


## Test views
def test_root(client):
    resp = client.get('/')
    assert resp.status_code == 400

def test_register(client):
    resp = client.post('/register', json={"username":"amir","password":"test"})
    assert resp.status_code == 200

def test_fail_register(client):
    resp = client.post('/register', json={"username":"amir","password":"test"})
    assert resp.status_code == 401

def test_login(client):
    resp = client.post('/login', json={"username":"amir","password":"test"})
    assert resp.status_code == 200

def test_fail_login(client):
    resp = client.post('/login', json={"username":"amir","password":"!!test!!"})
    assert resp.status_code == 400

def test_delete_user(client):
    resp = client.post('/delete', json={"username":"amir","password":"test"})
    assert resp.status_code == 200

def test_fail_delete_user(client):
    resp = client.post('/delete', json={"username":"!!amir!!","password":"test"})
    assert resp.status_code == 404