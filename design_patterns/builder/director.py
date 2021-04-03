from builder import builder

class director():
    def __init__(self) -> None:
        self._builder = None

    @property
    def  builder(self) -> builder:
        return self._builder

    @builder.setter
    def builder(self, builder: builder):
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()