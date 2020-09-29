from client import Client
from redwood_family.redwood_furniture_factory import RedwoodFurnitureFactory
from mahagony_family.mahagony_furniture_factory import MahagonyFurnitureFactory

if __name__ == "__main__":

    fac1 = Client(RedwoodFurnitureFactory())

    fac1.createChair()
    print(fac1.chair.sitOn())

    fac1.createSofa()
    print(fac1.sofa.sitOn())

    fac2 = Client(MahagonyFurnitureFactory())

    fac2.createChair()
    print(fac2.chair.sitOn())

    fac2.createSofa()
    print(fac2.sofa.sitOn())