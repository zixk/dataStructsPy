from ..interfaces.sofa import Sofa

class MahagonySofa(Sofa):

    def hasLegs(self) -> bool:
        return True

    def sitOn(self) -> str:
        return "Sat on a mahagony Sofa"