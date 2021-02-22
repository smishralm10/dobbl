import abc

class AbstractRespository(abc.ABC):

    def add(self, value):
        raise NotImplementedError

    def get(self, ref):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError