from ..adapters.repository import AbstractUserRepository
from ..domain.user import User

class UserAlreadyExistError(Exception):
    pass

def create_user(repository: AbstractUserRepository, username: str, password: str) -> User:
    ''' 
        If user doesn't exist, make a User instance with the username and password.
        Pass the instance to the create method of repository, 
        which in turn creates user in the database
    '''
    user = repository.get_by_username(username=username)

    if user:
        raise UserAlreadyExistError
    
    user = User.factory(username=username)
    user.set_password(password)
    return repository.create(user)

