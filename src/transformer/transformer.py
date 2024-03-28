from abc import ABC, abstractmethod


class BaseTransformer(ABC):

    @abstractmethod
    def transform(self, req, resp):
        pass