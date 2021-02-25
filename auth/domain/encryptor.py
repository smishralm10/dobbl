import abc
from passlib.hash import argon2

class AbstractEncryptor(abc.ABC):

    @abc.abstractclassmethod
    def encrypt(cls, value: str) -> str:
        pass

    @abc.abstractclassmethod
    def verify(cls, value: str, encrypted: str) -> bool:
        pass


class Encryptor(AbstractEncryptor):
    __salt = '897KMj$K'

    @classmethod
    def encrypt(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError('value to be encrypted should be a string')
        
        salt = str.encode(cls.__salt)
        return argon2.using(rounds=4, salt=salt).hash(value)

    @classmethod
    def verify(cls, value: str, encrypted: str):
        return argon2.verify(value, encrypted)
