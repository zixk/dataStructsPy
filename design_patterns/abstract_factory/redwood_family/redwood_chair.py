from ..interfaces.chair import Chair

class RedwoodChair(Chair):

    def hasLegs(self) -> bool:
        return True

    def sitOn(self) -> str:
        return "Sat on a redwood chair"