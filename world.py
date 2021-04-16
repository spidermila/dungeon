from typing import List

from clothes import Clothes
from item import Item
from player import Player
from room import Room
from weapon import Weapon

class World:
    def __init__(self, filename: str = 'default.map') -> None:
        self.rooms: List[Room] = []
        self.load_game(filename = filename)
        self.initialize_world()

    def load_game(self, filename = 'default.map') -> None:
        # open the file, load the contents into the self.data dict
        self.data: dict = {
            'name': 'default',
            'player': {
                'location': [1,1],
                'name': 'test guy',
                'HP': 30,
                'inventory_size': 15,
                'max_weight': 100,
                'inventory': [
                    {
                        'type': 'item',
                        'name': 'paper',
                        'weight': 1,
                        'size': 1,
                    },
                ],
                'equipped': {},
            },
            'rooms': [
                {
                    'location': [1,1],
                    'doors': [0, 1, 0, 0], # N E S W
                    'description': 'A small dark room. This is where it starts.',
                    'items': [
                        {
                            'type': 'clothes',
                            'name': 'vest',
                            'weight': 3,
                            'size': 4,
                            'color': 'gray',
                            'equippable': True,
                            'equippable_positions': ['torso'],
                        },
                        {
                            'type': 'weapon',
                            'name': 'dagger',
                            'weight': 1,
                            'size': 2,
                            'damage': 1,
                            'weapon_type': 'blade',
                            'twohanded': False,
                        },
                    ],
                    'mobs': [],
                },
                {
                    'location': [2,1],
                    'doors': [0, 0, 0, 1], # N E S W
                    'description': 'Small room with rocky floor.',
                    'items': [
                        {
                            'type': 'clothes',
                            'name': 'boots',
                            'weight': 3,
                            'size': 4,
                            'color': 'brown',
                            'equippable': True,
                            'equippable_positions': ['feet'],
                        },
                        {
                            'type': 'item',
                            'name': 'neco',
                            'weight': 2,
                            'size': 1,
                        },
                    ],
                    'mobs': [],
                },
            ],
        }

    def save_game(self, filename = 'default.map') -> None:
        pass

    def store_item_in_list(self, obj: dict, destination: List[Item]):
        if obj['type'] == 'clothes':
            destination.append(
                Clothes(
                    name = obj['name'],
                    weight = obj['weight'],
                    size = obj['size'],
                    color = obj['color'],
                    equippable = obj['equippable'],
                    equippable_positions = obj['equippable_positions'],
                ),
            )
        elif obj['type'] == 'item':
            destination.append(
                Item(
                    name = obj['name'],
                    weight = obj['weight'],
                    size = obj['size'],
                ),
            )
        elif obj['type'] == 'weapon':
            destination.append(
                Weapon(
                    name = obj['name'],
                    weight = obj['weight'],
                    size = obj['size'],
                    damage = obj['damage'],
                    weapon_type = obj['weapon_type'],
                    twohanded = obj['twohanded'],
                ),
            )

    def initialize_world(self) -> None:
        self.map_name = self.data['name']
        for room in self.data['rooms']:
            actual_room = Room(description = room['description'])
            actual_room.location = room['location']
            if actual_room.location == self.data['player']['location']:
                # spawn the player
                self.player = Player(room = actual_room)
                self.player.name = self.data['player']['name']
                self.player.HP = self.data['player']['HP']
                self.player.inventory_size = self.data['player']['inventory_size']
                self.player.max_weight = self.data['player']['max_weight']
                self.player.equippable_positions = ['head', 'body', 'left arm', 'right arm', 'hands', 'legs', 'feet']
                self.player.equipped = self.data['player']['equipped']
                for obj in self.data['player']['inventory']:
                    self.store_item_in_list(obj = obj, destination = self.player.inventory)
            actual_room.doors = room['doors']
            self.rooms.append(actual_room)
            for obj in room['items']:
                self.store_item_in_list(obj = obj, destination = actual_room.items)
            #for mob in room['mobs']:
            # TODO add mob spawning
