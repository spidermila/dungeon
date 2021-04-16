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
        self.separator_width = 60
        self.equippable_positions: List[str] = ['head', 'body', 'left arm', 'right arm', 'hands', 'legs', 'feet']
        self.equipped: dict = {}

    def minor_separator(self) -> None:
        print('-'*self.separator_width)

    def major_separator(self) -> None:
        print('='*self.separator_width)

    def equip(self, source: list, item: Item, position: str) -> bool:
        if position in self.equippable_positions:
            if position not in self.equipped.keys():
                self.equipped[position] = item
                # remove the item from the source
                source.pop(source.index(item))
                return True
            else:
                return False
        else:
            raise ValueError('Wrong position name')

    def unequip(self, destination: list, position: str) -> bool:
        if position in self.equippable_positions:
            if position in self.equipped.keys():
                item = self.equipped[position]
                self.equipped.pop(position)
                # add the unequipped item to the destination list
                destination.append(item)
                return True
            else:
                raise AssertionError('Unable to unequip item from this position. Position is marked as empty.')
        else:
            raise AssertionError('Wrong position name')

    def show_wearing(self) -> None:
        maxlen = 0
        for p in self.equippable_positions:
            if len(p) > maxlen:
                maxlen = len(p)
        self.major_separator()
        print(f'{"position":<{maxlen}} {"item":>10}')
        for position in self.equippable_positions:
            if position in self.equipped.keys():
                print(f'{position :<{maxlen}} {self.equipped[position].name :>10}')
            else:
                print(f'{position :<{maxlen}} {"-----":>10}')
        self.major_separator()

    def show_inventory(self) -> None:
        self.major_separator()
        print(f'Inventory: {self.get_current_inventory_occupation()}/{self.inventory_size} Weight: {self.get_current_weight()}/{self.max_weight}')
        self.minor_separator()
        if len(self.inventory) > 0:
            maxlen = 0
            for i in self.inventory:
                if len(i.name) > maxlen:
                    maxlen = len(i.name)
            print(f'{"item":<{maxlen}} {"size":>5} {"weight":>6}')
            for i in self.inventory:
                print(f'{i.name:<{maxlen}} {i.size :>5} {i.weight :>6}')
            self.major_separator()
        else:
            print('No items in inventory.')

    def look(self):
        self.major_separator()
        print(self.room.description)
        self.major_separator()
        if 1 in self.room.doors:
            # N E S W
            drs_map = {
                0: 'North',
                1: 'East',
                2: 'South',
                3: 'West',
            }
            drs = [drs_map[d] for d in [n for n, v in enumerate(list(map(lambda i: i == 1, self.room.doors))) if v]]
            print(f'Doors to the: {", ".join(drs)}')
        self.major_separator()
        if len(self.room.items) > 0:
            maxlen = 0
            for i in self.room.items:
                if len(i.name) > maxlen:
                    maxlen = len(i.name)
            print('Items in the room:')
            self.minor_separator()
            print(f'{"item":<{maxlen}} {"size":>5} {"weight":>6}')
            for i in self.room.items:
                print(f'{i.name :<{maxlen}} {i.size :>5} {i.weight :>6}')
        else:
            print('There are no items in the room.')
        self.major_separator()

    def get_current_weight(self) -> int:
        w = 0
        for i in self.equipped:
            w += self.equipped[i].weight
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
            self.major_separator()
            print('Which item number do you want to equip?')
            print('C/c or 0 for Cancel')
            self.minor_separator()
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
            p for p in self.equippable_positions \
            if p not in self.equipped.keys()
        ]
        if len(free_positions) > 0 and item.equippable:
            positions = list(set(item.equippable_positions).intersection(free_positions))
            if len(positions) > 0:
                if len(positions) == 1:
                    print(f'Equipping {item.name} at {positions[0]}')
                    self.equip(source = source, item = item, position = positions[0])
                    return True
                else:
                    self.minor_separator()
                    print('Equip at which position?')
                    print('C/c or 0 for Cancel')
                    self.minor_separator()
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
                print('Can not equip this item. No suitable positions found.')
        else:
            print('No free positions to equip anything')
        return False

    def unequip_dialog(self) -> bool:
        if len(self.equipped) > 0:
            self.major_separator()
            print('Which item number do you want to unequip?')
            print('C/c or 0 for Cancel')
            self.minor_separator()
            for i, position in enumerate(self.equipped):
                print(f'{i + 1}: {position}: {self.equipped[position].name}')
            while True:
                item_number = input('> ')
                if item_number in [str(i + 1) for i in range(len(self.equipped))]:
                    position = list(self.equipped.keys())[int(item_number) - 1]
                    break
                elif item_number.lower() in ['c', '0']:
                    return False
                else:
                    print('Wrong item number!')
            if self.get_current_inventory_occupation() + self.equipped[position].size <= self.inventory_size:
                print('1: Store in inventory')
                print('2: Drop to ground')
                while True:
                    destination_number = input('> ')
                    if destination_number == '1':
                        self.unequip(position = position, destination = self.inventory)
                        print('Done')
                        return True
                    elif destination_number == '2':
                        self.unequip(position = position, destination = self.room.items)
                        print('Done')
                        return True
                    else:
                        print('Wrong destination number!')
            else:
                print('Not enough space in the inventory. Dropping the item to the ground.')
                return False
        return False

    def pickup_dialog(self) -> bool:
        if len(self.room.items) > 0:
            self.major_separator()
            print('Which item number do you want to pick up?')
            print('C/c or 0 for Cancel')
            self.minor_separator()
            for i, item in enumerate(self.room.items):
                print(f'{i + 1}: {item.name}')
            while True:
                item_number = input('> ')
                if item_number in [str(i + 1) for i in range(len(self.room.items))]:
                    item = self.room.items[int(item_number) - 1]
                    break
                elif item_number.lower() in ['c', '0']:
                    return False
                else:
                    print('Wrong item number!')
            if self.get_current_inventory_occupation() + item.size <= self.inventory_size:
                self.inventory.append(item)
                self.room.items.pop(self.room.items.index(item))
                print(f'Picked up {item.name} from the ground.')
                return True
            else:
                print(f'There is not enough space in your inventory.')
        return False

    def drop_dialog(self) -> bool:
        if len(self.inventory) > 0:
            self.major_separator()
            print('Which item number do you want to drop?')
            print('C/c or 0 for Cancel')
            self.minor_separator()
            for i, item in enumerate(self.inventory):
                print(f'{i + 1}: {item.name}')
            while True:
                item_number = input('> ')
                if item_number in [str(i + 1) for i in range(len(self.inventory))]:
                    item = self.inventory[int(item_number) - 1]
                    break
                elif item_number.lower() in ['c', '0']:
                    return False
                else:
                    print('Wrong item number!')
            self.room.items.append(item)
            self.inventory.pop(self.inventory.index(item))
            print(f'Dropped {item.name} to the ground.')
        else:
            print('Inventory is empty')
        return False
