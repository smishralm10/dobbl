import re
from typing import Optional
from ..domain.encryptor import Encryptor, AbstractEncryptor

class PasswordStrengthError(Exception):
    pass

class InvalidEmailAddress(Exception):
    pass


class Password:
    def __init__(self, encryptor: AbstractEncryptor, value: Optional[str]=None):
        self._value = value
        self._encryptor = encryptor

    def __repr__(self) -> str:
        return f'<Password object {self._value}'
    
    def __eq__(self, value: str) -> bool:
        return self._encryptor.verify(value, self._value)
    
    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, value: str) -> str:
        valid_password, _ = self.validate_strength(value)
        if not valid_password:
            raise PasswordStrengthError(
            '''Password should be 8 characters long,
               must contain atleast 1 digit, 1 symbol,
               1 uppercase letter and 1 lowercase letter'''
        )

        self._value = self._encryptor.encrypt(value)

    @classmethod
    def validate_strength(cls, value: str) -> bool:
        if value is None:
            return False, {}

        length = cls._validate_length(value)
        digit = cls._validate_digit(value)
        uppercase = cls._validate_uppercase(value)
        lowercase = cls._validate_lowercase(value)
        symbol = cls._validate_symbol(value)

        valid = all([length, digit, uppercase, lowercase, symbol])
        error_dict = {
            'length': length,
            'digit': digit,
            'uppercase': uppercase,
            'lowercase': lowercase,
            'symbol': symbol,
        }

        return valid, error_dict

    @classmethod
    def _validate_length(cls, value: str) -> bool:
        return len(value) >= 8
    
    @classmethod
    def _validate_digit(cls, value: str) -> bool:
        return bool(re.search(r'\d', value))
    
    @classmethod
    def _validate_uppercase(cls, value: str) -> bool:
        return bool(re.search(r'[A-Z]', value))
    
    @classmethod
    def _validate_lowercase(cls, value: str) -> bool:
        return bool(re.search(r'[a-z]', value))
    
    @classmethod
    def _validate_symbol(cls, value: str) -> bool:
        return bool(re.search(r'\W', value))


class Email:
    def __init__(self, email: str):
        self._email = email
    
    @property
    def value(self):
        return self._email
    
    @value.setter
    def value(self, email: str):
        valid_email = validate_email(email)

        if not valid_email:
            raise InvalidEmailAddress('Email is invalid')

        self._email = email
    
    @staticmethod
    def validate_email(email: str):
        return bool(re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email))
    