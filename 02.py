# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "injector"
# ]
# ///

from injector import Injector, inject

# ============================ Repository ============================

from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_data(self):
        pass


class MyRepository(IRepository):
    def get_data(self):
        return "Hello from MyRepository!"


# ============================ Service ============================


class MyService:
    @inject
    def __init__(self, my_repository: IRepository):
        self.my_repository = my_repository

    def get_data(self):
        return self.my_repository.get_data()


# ============================ Controller ============================


class MyController:
    @inject
    def __init__(self, my_service: MyService):
        self.my_service = my_service

    def get_data(self):
        return self.my_service.get_data()


# ============================ Config ============================


def configure_injector() -> Injector:
    injector = Injector()
    injector.binder.bind(IRepository, to=MyRepository)
    return injector


injector = configure_injector()
my_controller = injector.get(MyController)
data = my_controller.get_data()
print(data)
