from __future__ import annotations

from typing import Any
from typing import List

from connection import Connection
from item import Item

class Room:
    '''Door's index and Connection index determine which door belongs to which connection.'''
    def __init__(self, id: int, description: str) -> None:
        self.connections: list[Connection] = []
        self.description = description
        #self.doors: List[Door] = []
        self.id = id
        self.items: list[Item] = []
        self.location: list[int] = []

    def get_all_connections_by_ids(self) -> list:
        conns: list[Any] = []
        ids: list[int] = []
        for c in self.connections:
            for r in c.rooms:
                assert isinstance(r, Room)
                ids.append(r.id)
            conns.append(ids.sort())
        return conns

    #def add_door(self, direction: str, material: str, opened: bool, locks: List[Lock]) -> None:
    #    self.doors.append(Door(room=self))

    def print_doors(self) -> None:
        for connection in self.connections:
            for door in connection.doors:
                if door.opened:
                    opened = 'Open'
                else:
                    opened = 'Closed'
                connected_room = connection.get_opposite_room(self)
                if isinstance(connected_room, Room):
                    print(f'{opened} {door.material} door leading to room number {connected_room.id}')
