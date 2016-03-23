from abc import abstractmethod


class AbstractSeed(object):
    @abstractmethod
    def seed(self):
        raise NotImplementedError
