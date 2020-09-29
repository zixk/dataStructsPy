from interfaces.furniture_factory import FurnitureFactory

class Client():
    def __init__(self, factory: FurnitureFactory):
        self.factory = factory
        self.chair = None
        self.sofa = None

    def createChair(self):
        self.chair = self.factory.createChair()

    def createSofa(self):
        self.sofa = self.factory.createSofa()

    