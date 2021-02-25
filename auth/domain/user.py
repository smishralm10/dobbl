import abc
from typing import Optional
from uuid import uuid4, UUID
from .encryptor import Encryptor, AbstractEncryptor
from ..value_object.values import Password, Email


class UserValueError(Exception):
    pass

class User:
    def __init__(
        self, uuid: UUID, username: str, email: Optional[str]=None, password: Optional[str]=None, 
        encryptor: AbstractEncryptor=Encryptor, active: Optional[bool]=True
        ):

        self._uuid = uuid
        self._username = username
        self._email = Email(email)
        self._password = Password(encryptor, password)
        self._active = active

    @property
    def uuid(self) -> UUID:
        return self._uuid
    
    @property
    def username(self) -> str:
        return self._username
    
    @property
    def email(self) -> str:
        return self._email.value
    
    @property
    def password(self) -> str:
        return self._password.value
    
    @property
    def active(self) -> str:
        return self._active
    
    def set_password(self, value: str) -> None:
        self._password.value = value

    def verify_password(self, value: str) -> bool:
        return self._password.value == value
    
    def verify_email(self, value: str) -> bool:
        return self._email.value == value
    
    def deactivate(self):
        self._active = False

    @classmethod
    def factory(cls, 
                username: str, 
                password: Optional[str]=None, 
                email: Optional[str]=None,
                uuid: Optional[UUID]=None, 
                active: Optional[bool]=True  
    ):
        uuid = uuid or uuid4()

        if not username:
            raise UserValueError('username is required')

        return cls(
            uuid=uuid,
            username=username,
            password=password,
            email=email,
            active=active
        )