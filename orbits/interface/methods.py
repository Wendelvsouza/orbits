from abc import ABC, abstractmethod
from typing import Dict, Union, List


class MethodsInterface(ABC):
    @abstractmethod
    def call(
        self,
        const: Dict[str, float],
        step: Dict[str, float],
        mars: Dict[str, Union[float, list]],
        earth: Dict[str, Union[float, list]],
    ) -> List[int]:
        pass
