from typing import Dict
from typing import List

from item import Item
from room import Room

class Player:
    def __init__(self, room: Room) -> None:
        self.room = room
        self.name: str = ''
        self.inventory: List[Item] = []
        self.HP: int = 30
        self.inventory_size = 10
        self.max_weight = 100
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

    def unequip(self, destination: list, position: str) -> bool:
        if position in self.equippable_positions_occupied:
            if self.equippable_positions_occupied[position]:
                item = self.wearing[position]
                self.wearing.pop(position)
                self.equippable_positions_occupied[position] = False
                # add the unequipped item to the destination list
                destination.append(item)
                return True
            else:
                raise AssertionError('Unable to unequip item from this position. Position is marked as empty.')
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

    def get_current_weight(self) -> int:
        w = 0
        for i in self.wearing:
            w += i.weight
        for i in self.inventory:
            w += i.weight
        return w

    def get_current_inventory_occupation(self) -> int:
        o = 0
        for i in self.inventory:
            o += i.size
        return o

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
