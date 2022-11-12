import pytest
from authenticate.model.models import User



@pytest.fixture
def new_user():
    user = User(username='test_username', password='testpassword')
    return user

## Test model

def test_new_user(new_user):

    assert new_user.username == 'test_username'
    assert new_user.password != 'testpassword'


