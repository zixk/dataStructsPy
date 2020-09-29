from abc import ABC, abstractmethod
from .chair import Chair
from .sofa import Sofa

class FurnitureFactory(ABC):

    @abstractmethod
    def createChair(self) -> Chair:
        pass

    @abstractmethod
    def createSofa(self) -> Sofa:
        pass