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
        self.equippable = False
        self.equippable_positions: list = []

class Clothes(Item):
    type = 'clothes'
    def __init__(self, color: str, equippable_positions: List[str], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color
        self.equippable = True
        self.equippable_positions = equippable_positions

class Weapon(Item):
    type = 'weapon'
    def __init__(self, damage: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.damage = damage

class Player:
    def __init__(self, room: Room) -> None:
        self.room = room
        self.name: str = ''
        self.inventory: List[Item] = []
        self.HP: int = 30
        self.equippable_positions_occupied: Dict[str, bool] = {
            'head': False,
            'body': False,
            'left arm': False,
            'right arm': False,
            'hands': False,
            'legs': False,
            'feet': False,
        }
        self.wearing: dict = {}

    def equip(self, source: list, item: Item, position: str) -> bool:
        if position in self.equippable_positions_occupied:
            if not self.equippable_positions_occupied[position]:
                self.wearing[position] = item
                self.equippable_positions_occupied[position] = True
                # remove the item from the source
                source.pop(source.index(item))
                return True
            else:
                return False
        else:
            raise ValueError('Wrong position name')

    def strip(self, destination: list, position: str) -> bool:
        if position in self.equippable_positions_occupied:
            if self.equippable_positions_occupied[position]:
                item = self.wearing[position]
                self.wearing.pop(position)
                self.equippable_positions_occupied[position] = False
                # add the stripped item to the destination list
                destination.append(item)
                return True
            else:
                raise AssertionError('Unable to strip clothes from this position. Position is marked as empty.')
        else:
            raise AssertionError('Wrong position name')

    def show_wearing(self) -> None:
        for k in self.equippable_positions_occupied:
            if self.equippable_positions_occupied[k]: # occupied position
                print(f'{k}: {self.wearing[k].name}')
            else:
                print(f'{k}: -')

    def show_inventory(self) -> None:
        for i in self.inventory:
            print(i.name)

    def look(self):
        print(self.room.description)
        if len(self.room.items) > 0:
            print('Items in the room:')
            for i in self.room.items:
                print(i.name)
        else:
            print('There are no items in the room')

    def equip_dialog(self) -> bool:
        items_in_reach: list = []
        for item in self.room.items:
            if item.equippable:
                items_in_reach.append([item, self.room.items])
        for item in self.inventory:
            if item.equippable:
                items_in_reach.append([item, self.inventory])
        if len(items_in_reach) > 0:
            print('Which item do you want to equip?')
            print('C/c or 0 for Cancel')
            for i, item_source_pair in enumerate(items_in_reach):
                print(f'{i + 1}: {item_source_pair[0].name}')
            while True:
                item_number = input('> ')
                if item_number in [str(i + 1) for i in range(len(items_in_reach))]:
                    item = items_in_reach[int(item_number) - 1][0]
                    source = items_in_reach[int(item_number) - 1][1]
                    break
                elif item_number.lower() in ['c', '0']:
                    return False
                else:
                    print('Wrong item number!')
        else:
            print('Nothing to equip.')
            return False
        free_positions = [
            p for p in self.equippable_positions_occupied \
            if self.equippable_positions_occupied[p] == False
        ]
        if len(free_positions) > 0 and item.equippable:
            positions = list(set(item.equippable_positions).intersection(free_positions))
            if len(positions) > 0:
                if len(positions) == 1:
                    print(f'Equipping {item.name} at {positions[0]}')
                    self.equip(source = source, item = item, position = positions[0])
                    return True
                else:
                    print('Equip at which position?')
                    print('C/c or 0 for Cancel')
                    for i, position in enumerate(positions):
                        print(f'{i + 1}: {position}')
                    while True:
                        position_number = input('> ')
                        if position_number in [str(i + 1) for i in range(len(positions))]:
                            print(f'Equipping {item.name} at {positions[int(position_number) - 1]}')
                            self.equip(source = source, item = item, position = positions[int(position_number) - 1])
                            return True
                        elif position_number.lower() in ['c', '0']:
                            return False
                        else:
                            print('Wrong position number!')

        else:
            print('No free positions to equip anything')
        return False

    def unequip_dialog(self) -> None:
        ...


def main():
    world = World()
    world.rooms.append(Room(id = 1, description = 'A small dark room'))
    p = Player(room = world.rooms[0])
    p.inventory.append(Item(name = 'neco', weight = 2))
    p.inventory.append(Clothes(name = 'shirt', equippable_positions = ['body', 'legs'], weight = 2, color = 'red'))
    p.inventory.append(Weapon(name = 'dagger', weight = 1, damage = 1))
    p.room.items.append(Clothes(name = 'simple hat', equippable_positions = ['head'], weight = 1, color = 'gray'))

    commands = {
        'quit commands': ['q', 'quit', 'exit'],
        'help commands': ['h', 'help'],
        'character commands': ['c', 'char', 'character'],
        'inventory commands': ['i', 'inv', 'inventory'],
        'look commands': ['l', 'look'],
        'equip commands': ['equip'],
        'unequp commands': ['unequip', 'un'],
    }

    while True:
        command_line = input(': ')
        command = command_line.lower().split()[0]
        if command in commands['quit commands']:
            break
        elif command in commands['help commands']:
            for c in commands:
                print(f'{c}: {commands[c]}')
        elif command in commands['character commands']:
            p.show_wearing()
        elif command in commands['inventory commands']:
            p.show_inventory()
        elif command in commands['look commands']:
            p.look()
        elif command in commands['equip commands']:
            p.equip_dialog()
        elif command in commands['unequip commands']:
            p.unequip_dialog()
        else:
            print('Unknown command')


if __name__ == '__main__':
    exit(main())
