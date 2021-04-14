'''\
        Learning Python
'''
from clothes import Clothes
from item import Item
from player import Player
from room import Room
from weapon import Weapon
from world import World

def main():
    world = World()
    world.rooms.append(Room(id = 1, description = 'A small dark room'))
    p = Player(room = world.rooms[0])
    p.inventory.append(Item(name = 'paper', weight = 1, size = 1))
    p.inventory.append(Clothes(name = 'shirt', equippable_positions = ['body'], weight = 10, size = 2, color = 'red'))
    p.inventory.append(Weapon(name = 'dagger of your ancestors', weight = 1, size = 1, damage = 1))
    p.room.items.append(Clothes(name = 'simple hat', equippable_positions = ['head'], weight = 1, size = 2, color = 'gray'))

    commands = {
        'quit commands': ['q', 'quit', 'exit'],
        'help commands': ['h', 'help'],
        'character commands': ['c', 'char', 'character'],
        'inventory commands': ['i', 'inv', 'inventory'],
        'look commands': ['l', 'look'],
        'equip commands': ['eq', 'equip'],
        'unequip commands': ['un', 'unequip'],
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
