import abc
from uuid import UUID
from domain.user import User
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist


class AbstractUserRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, uuid: UUID) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError


class DjangoUserRepository(AbstractUserRepository):

    def __init__(self, model: Model):
        self._model = model
    
    def get(self, uuid: UUID) -> User:
        try:
            instance = self._model.objects.get(uuid=uuid)
        except ObjectDoesNotExist:
            return None
        
        return self._factory_user(instance)
        
    def update(self, user: User) -> User:
        self._model.objects.filter(uuid=user.uuid).update(username=user.username, active=user.active)
        return self.get(uuid=user.uuid)

    def update_password(self, user: User) -> User:
        self._model.objects.filter(uuid=user.uuid).update(password=user.password)
        return self.get(uuid=user.uuid)

    def create(self, user: User) -> User:
        instance = self._model.objects.create(username=user.username,
                                              password=user.password,
                                              uuid=user.uuid,
                                              active=user.active)
        return self._factory_user(instance)
    
    def _factory_user(self, instance: Model) -> User:
        return User.factory(
            uuid=instance.uuid,
            username=instance.username,
            password=instance.password,
            active=instance.active
        )

