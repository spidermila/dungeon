'''\
        Learning Python
'''
from os import system
from sys import platform

from clothes import Clothes
from item import Item
from player import Player
from room import Room
from weapon import Weapon
from world import World

def main():
    world = World()
    world.load_game()
    p = world.player
    status = True
    #world.rooms.append(Room(id = 1, description = 'A small dark room with no doors or windows. \nYou are trapped.'))
    #p.inventory.append(Item(name = 'paper', weight = 1, size = 1))
    #p.inventory.append(Clothes(name = 'shirt', equippable_positions = ['body'], weight = 10, size = 2, color = 'red'))
    #p.inventory.append(Weapon(name = 'dagger of your ancestors', weight = 1, size = 1, damage = 1))
    #p.room.items.append(Clothes(name = 'simple hat', equippable_positions = ['head'], weight = 1, size = 2, color = 'gray'))

    if platform.find('linux') != -1:
        cls_command = 'clear'
    elif platform.find('win') != -1:
        cls_command = 'cls'
    elif platform.find('darwin') != -1:
        cls_command = 'clear'
    else:
        print('Unknown OS. cls will not work!')
        cls_command = False # type: ignore

    def cls() -> None:
        if cls_command: system(cls_command)

    commands = {
        'quit commands': ['q', 'quit', 'exit'],
        'help commands': ['h', 'help'],
        'move commands': ['m', 'mo', 'move'],
        'character commands': ['c', 'char', 'character'],
        'inventory commands': ['i', 'inv', 'inventory'],
        'look commands': ['l', 'look'],
        'equip commands': ['eq', 'equip'],
        'unequip commands': ['un', 'unequip'],
        'pickup commands': ['pi', 'pickup'],
        'drop commands': ['dr', 'drop'],
        'toggle status': ['st'],
    }

    cls()
    while True:
        if status:
            #cls()
            p.look()
            p.show_inventory()
            p.show_wearing()

        command_line = input(': ')
        if len(command_line) > 0:
            command = command_line.lower().split()[0]
            if command in commands['quit commands']:
                break
            elif command in commands['help commands']:
                cls()
                for c in commands:
                    print(f'{c}: {commands[c]}')
            elif command in commands['move commands']:
                cls()
                p.move_dialog()
            elif command in commands['character commands']:
                cls()
                if not status: p.show_wearing()
            elif command in commands['inventory commands']:
                cls()
                if not status: p.show_inventory()
            elif command in commands['look commands']:
                cls()
                if not status: p.look()
            elif command in commands['equip commands']:
                cls()
                p.equip_dialog()
            elif command in commands['unequip commands']:
                cls()
                p.unequip_dialog()
            elif command in commands['pickup commands']:
                cls()
                p.pickup_dialog()
            elif command in commands['drop commands']:
                cls()
                p.drop_dialog()
            elif command in commands['toggle status']:
                cls()
                if status:
                    status = False
                else:
                    status = True
            else:
                cls()
                print('')
                print('Unknown command')
                print('')


if __name__ == '__main__':
    exit(main())
