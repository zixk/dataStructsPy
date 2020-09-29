from interfaces.furniture_factory import FurnitureFactory
from .redwood_chair import RedwoodChair
from .redwood_sofa import RedwoodSofa

class RedwoodFurnitureFactory(FurnitureFactory):

    def createChair(self):
        return RedwoodChair()

    def createSofa(self):
        return RedwoodSofa()