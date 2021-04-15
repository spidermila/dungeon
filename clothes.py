from typing import List

from item import Item

class Clothes(Item):
    type = 'clothes'
    def __init__(self, color: str, equippable: bool, equippable_positions: List[str], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color
        self.equippable = True
        self.equippable_positions = equippable_positions
