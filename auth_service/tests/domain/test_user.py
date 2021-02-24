import pytest
from uuid import uuid4, UUID
from auth_service.domain.user import User, UserValueError

class TestFactory:
    

    def test_adds_uuid_when_uuid_is_not_set(self):
        user = User.factory('username', 'Password@13')
        assert isinstance(user.uuid, UUID)
    
    def test_uses_the_assigned_uuid(self):
        uuid = uuid4()
        user = User.factory(uuid=uuid, username='username', password='Password@13')
        assert uuid == user.uuid
    
    def test_when_has_no_username_raises_value_error(self):
        with pytest.raises(UserValueError):
            user = User.factory(username=None, password='Password@13')
        
    def test_verifies_password_correctly(self):
        password = 'Password@13'
        user = User.factory('username', password=password)
        assert user.password == password
        
