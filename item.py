class Item:
    type = 'item'

    def __init__(self, name: str, weight: int, size: int) -> None:
        self.name = name
        self.weight = weight
        self.size = size
        self.equippable = False
        self.equippable_positions: list = []
