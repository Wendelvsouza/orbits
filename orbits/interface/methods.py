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
    ) -> List[float]:
        """
        Abstract method to be implemented by subclasses.

        Parameters:
        const: (Dict[str, float])
                A dictionary containing parameters to be considered as
                constants.

        step: (Dict[str, float])
                A dictionary containing step values for computation.


        mars: (Dict[str, Union[float, list]])
                A dictionary representing Mars, with its attributes
                represented as key-value pairs. The values can either be
                floats or lists.

        earth: (Dict[str, Union[float, list]])
                A dictionary representing Earth, with its attributes
                represented as key-value pairs. The values can either be
                floats or lists.

        Returns:
                    This function returns a list of float.
        """

        raise NotImplementedError("Subclasses must implement this abstract method")
