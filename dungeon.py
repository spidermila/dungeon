'''\
        Learning Python
'''
from typing import Dict
from typing import List
from typing import Union

class World:
    def __init__(self) -> None:
        self.rooms: List[Room] = []

class Room:
    def __init__(self, id: int, description: str) -> None:
        self.id = id
        self.items: List[Item] = []
        self.connections: List[int] = []
        self.description = description

    def connect_to(self, room_ids: list) -> None:
        for r in room_ids:
            self.connections.append(r)

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
    def __init__(self, room: Room) -> None:
        self.room = room
        self.name: str = ''
        self.items: List[Item] = []
        self.HP: int = 30
        self.wearable_positions_occupied: Dict[str, bool] = {
            'head': False,
            'body': False,
            'left arm': False,
            'right arm': False,
            'hands': False,
            'legs': False,
            'feet': False,
        }
        self.wearing = {} # type: ignore

    def wear(self, source: list, item: Clothes, position: str) -> bool:
        if position in self.wearable_positions_occupied:
            if not self.wearable_positions_occupied[position]:
                self.wearing[position] = item
                self.wearable_positions_occupied[position] = True
                # remove the item from the source
                source.pop(source.index(item))
                return True
            else:
                return False
        else:
            raise ValueError('Wrong position name')

    def strip(self, destination: list, position: str) -> bool:
        if position in self.wearable_positions_occupied:
            if self.wearable_positions_occupied[position]:
                item = self.wearing[position]
                self.wearing.pop(position)
                self.wearable_positions_occupied[position] = False
                # add the stripped item to the destination list
                destination.append(item)
                return True
            else:
                raise AssertionError('Unable to strip clothes from this position. Position is marked as empty.')
        else:
            raise AssertionError('Wrong position name')

    def show_wearing(self) -> None:
        for k in self.wearable_positions_occupied:
            if self.wearable_positions_occupied[k]: # occupied position
                print(f'{k}: {self.wearing[k].name}')
            else:
                print(f'{k}: -')

    def show_inventory(self) -> None:
        for i in self.items:
            print(i.name)

    def look(self):
        print(self.room.description)
        if len(self.room.items) > 0:
            print('Items in the room:')
            for i in self.room.items:
                print(i.name)
        else:
            print('There are no items in the room')


def main():
    world = World()
    world.rooms.append(Room(id = 1, description = 'A small dark room'))
    p = Player(room = world.rooms[0])
    p.items.append(Item(name = 'neco', weight = 2))
    p.items.append(Clothes(name = 'shirt', wearable_positions = ['body'], weight = 2, color = 'red'))
    p.items.append(Weapon(name = 'dagger', weight = 1, damage = 1))
    p.room.items.append(Clothes(name = 'simple hat', wearable_positions = ['head'], weight = 1, color = 'gray'))

    commands = {
        'quit commands': ['q', 'quit', 'exit'],
        'help commands': ['h', 'help'],
        'character commands': ['c', 'char', 'character'],
        'inventory commands': ['i', 'inv', 'inventory'],
        'look commands': ['l', 'look'],
    }

    while True:
        command = input(': ')
        if command.lower() in commands['quit commands']:
            break
        elif command.lower() in commands['help commands']:
            for c in commands:
                print(f'{c}: {commands[c]}')
        elif command.lower() in commands['character commands']:
            p.show_wearing()
        elif command.lower() in commands['inventory commands']:
            p.show_inventory()
        elif command.lower() in commands['look commands']:
            p.look()
        else:
            print('Unknown command')


if __name__ == '__main__':
    exit(main())
