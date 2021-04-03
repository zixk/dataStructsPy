from builder import builder
from car import car


class car_builder(builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = car()

    @property
    def product(self) -> car:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")
