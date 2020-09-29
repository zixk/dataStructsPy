from interfaces.furniture_factory import FurnitureFactory
from .mahagony_chair import MahagonyChair
from .mahagony_sofa import MahagonySofa

class MahagonyFurnitureFactory(FurnitureFactory):

    def createChair(self):
        return MahagonyChair()

    def createSofa(self):
        return MahagonySofa()