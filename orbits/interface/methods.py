from abc import ABC, abstractmethod
from typing import Dict, Union


class MethodsInterface(ABC):
    @abstractmethod
    def methods(
        self,
        const: Dict[str, float],
        step: Dict[str, float],
        mars: Dict[str, Union[float, list]],
        earth: Dict[str, Union[float, list]],
    ) -> None:
        pass
