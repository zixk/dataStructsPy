from interfaces.sofa import Sofa

class RedwoodSofa(Sofa):

    def hasLegs(self) -> bool:
        return True

    def sitOn(self) -> str:
        return "Sat on a redwood Sofa"