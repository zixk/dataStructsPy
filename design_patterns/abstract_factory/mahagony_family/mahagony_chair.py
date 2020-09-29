from ..interfaces.chair import Chair

class MahagonyChair(Chair):

    def hasLegs(self) -> bool:
        return True

    def sitOn(self) -> str:
        return "Sat on a mahagony chair"