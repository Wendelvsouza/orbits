from abc import ABC, abstractmethod


class MethodsInterface(ABC):
    @abstractmethod
    def methods(self) -> list:
        pass
