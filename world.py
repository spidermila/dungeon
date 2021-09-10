from __future__ import annotations

import io
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional

try:
    import yaml
except(NameError, ModuleNotFoundError):
    import sys
    print('PyYAML is needed for this game.')
    raise ImportError(f'PyYAML is needed for this game.\nInstall it: {sys.executable} -m pip install PyYAML')


from clothes import Clothes
from connection import Connection
from item import Item
from player import Player
from room import Room
from weapon import Weapon

class World:
    def __init__(self) -> None:
        self.rooms: list[Room] = []
        self.connections: list[Connection] = []
        self.data: dict = {}

    def load_game(self, filename: str) -> None:
        if Path(filename).is_file():
            with open(filename, 'r') as stream:
                try:
                    self.data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        else:
            print(f"File {filename} doesn't exist.")
            # TODO generate a map or something...
            exit()
        self.initialize_world()

    def save_game(self, filename = 'default_game.yaml') -> None:
        with io.open(filename, 'w', encoding='utf8') as outfile:
            yaml.dump(self.data, outfile, default_flow_style=False, allow_unicode=True)

    def store_item_in_list(self, obj: dict, destination: list[Item]):
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

    def get_room_by_id(self, room_id: int) -> Room | None:
        for room in self.rooms:
            if room.id == room_id:
                return room
        return None

    def initialize_world(self) -> None:
        self.map_name = self.data['name']
        # initial room creation
        for room in self.data['rooms']:
            actual_room = Room(id = room['id'], description = room['description'])
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
            self.rooms.append(actual_room)
            for obj in room['items']:
                self.store_item_in_list(obj = obj, destination = actual_room.items)
            #for mob in room['mobs']:
            # TODO add mob spawning
        # add connections
        for connection in self.data['connections']:
            r1,r2 = connection['connection']
            self.connections.append(Connection(self))
            self.connections[-1].load_connection(connection)
        #breakpoint()
