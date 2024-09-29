# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "injector"
# ]
# ///

from injector import Injector, inject
from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_data(self):
        pass


class MyService:
    @inject
    def __init__(self, my_repository: IRepository):
        self.my_repository = my_repository

    def get_data(self):
        return self.my_repository.get_data()


class MyRepository(IRepository):
    def get_data(self):
        return "Hello from MyRepository!"


injector = Injector()
injector.binder.bind(IRepository, to=MyRepository)
my_service = injector.get(MyService)
print(my_service.get_data())
