from __future__ import annotations

from typing import Any
from typing import List

from door import *
from item import Item

class Room:
    '''Door's index and Connection index determine which door belongs to which connection.'''
    def __init__(self, id: int, description: str) -> None:
        self.connections: List[Connection] = []
        self.description = description
        self.doors: List[Door] = []
        self.id = id
        self.items: List[Item] = []
        self.location: List[int] = []

    def connect_to_room(self, room: Room) -> None:
        self.connections.append(Connection(self, room))

    def get_all_connections_by_ids(self) -> list:
        conns: List[Any] = []
        ids: List[int] = []
        for c in self.connections:
            for r in c.rooms:
                ids.append(r.id)
            conns.append(ids.sort())
        return conns

    def load_doors(self, door_list: List[dict]) -> None:
        for door in door_list:
            self.doors.append(Door(self))
            self.doors[-1].direction = door['direction']
            self.doors[-1].material = door['material']
            self.doors[-1].opened = door['opened']
            for lock in door['locks']:
                self.doors[-1].locks.append(
                    Lock(
                        material=lock['material'],
                        locked=lock['locked'],
                        diff=lock['diff'],
                    ),
                )

    def add_door(self, direction: str, material: str, opened: bool, locks: List[Lock]) -> None:
        self.doors.append(Door(room=self))

    def print_doors(self) -> None:
        for door in self.doors:
            if door.opened:
                opened = 'Open'
            else:
                opened = 'Closed'
            print(f'{opened} {door.material} door to the {door.direction}')

class Connection:
    def __init__(self, n1: Room, n2: Room) -> None:
        self.rooms: List[Room] = [n1, n2]
