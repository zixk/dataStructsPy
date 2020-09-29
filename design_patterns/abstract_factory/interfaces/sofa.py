from abc import ABC, abstractmethod

class Sofa(ABC):
    
    @abstractmethod
    def hasLegs(self) -> bool:
        pass

    @abstractmethod
    def sitOn(self) -> str:
        pass