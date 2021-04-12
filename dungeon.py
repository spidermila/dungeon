'''\
        Learning Python
'''
from typing import Dict
from typing import List
from typing import Union

class Room:
    def __init__(self, id: int) -> None:
        self.id = id
        self.items: List[Item] = []
        self.connections: List[int] = []
        self.description = ''

    def connect_to(self, room_ids: list) -> None:
        for r in room_ids:
            self.connections.append(r)

class Dungeon:
    def __init__(self) -> None:
        self.rooms: List[Room] = []

    def create_room(self) -> None:
        if len(self.rooms) == 0:
            self.rooms.append(Room(0))

class Item:
    type = 'item'
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

class Clothes(Item):
    type = 'clothes'
    def __init__(self, color: str, wearable_positions: List[str], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color
        self.wearable = True
        self.wearable_positions = wearable_positions

class Weapon(Item):
    type = 'weapon'
    def __init__(self, damage: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.damage = damage

class Player:
    def __init__(self) -> None:
        self.name: str = ''
        self.items: List[Item] = []
        self.HP: int = 30
        self.wearable_positions: Dict[str, Union[None, Clothes]] = {
            'head': None,
            'body': None,
            'left arm': None,
            'right arm': None,
            'hands': None,
            'legs': None,
            'feet': None,
        }

    def wear(self, source: list, item: Clothes, position: str) -> bool:
        if position in self.wearable_positions:
            if self.wearable_positions[position] == None:
                self.wearable_positions[position] = item
                # remove the item from the source
                source.pop(source.index(item))
                return True
            else:
                return False
        else:
            raise ValueError('Wrong position name')

    def show_wearing(self) -> None:
        for k in self.wearable_positions.keys():
            if isinstance(self.wearable_positions[k], Clothes):
                print(f'{k}: {self.wearable_positions[k].name}')
            else:
                print(f'{k}: -')

    def show_inventory(self) -> None:
        for i in self.items:
            print(i.name)

def main():
    p = Player()
    p.items.append(Item(name = 'neco', weight = 2))
    p.items.append(Clothes(name = 'shirt', wearable_positions = ['body'], weight = 2, color = 'red'))
    p.items.append(Weapon(name = 'dagger', weight = 1, damage = 1))
    p.wear(source = p.items, item = p.items[1], position = 'body')
    p.show_inventory()
    p.show_wearing()



if __name__ == '__main__':
    exit(main())
