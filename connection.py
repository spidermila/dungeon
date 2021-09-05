from __future__ import annotations

from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING: # thank you Anthony! https://www.youtube.com/watch?v=B5cjckVzY4g
    from room import Room
    from world import World

class Connection:
    def __init__(self, world: World) -> None:
        self.rooms: List[Optional[Room]] = []
        self.doors: List[Door] = []
        self.world = world

    def load_connection(self, connection_dict: dict) -> None:
        self.connected_room_ids = connection_dict['connection']
        for id in self.connected_room_ids:
            self.rooms.append(self.world.get_room_by_id(id))
            assert isinstance(self.rooms[-1], Room)
            self.rooms[-1].connections.append(self)
        for door in connection_dict['doors']:
            self.doors.append(Door())
            current_door = self.doors[-1]
            current_door.material = door['material']
            current_door.opened = door['opened']
            for lock in door['locks']:
                current_door.locks.append(Lock())
                current_lock = current_door.locks[-1]
                current_lock.material = lock['material']
                current_lock.diff = lock['diff']
                current_lock.locked = lock['locked']

    def get_opposite_room(self, room: Room) -> Optional[Room]:
        for r in self.rooms:
            if r != room:
                return r
        return room

class Door:
    def __init__(self) -> None:
        self.material: str = ''
        self.opened: bool = False
        self.locks: List[Lock] = []

    def open_door(self) -> bool:
        if self.opened:
            print('The door is already open.')
            return False
        else:
            for lock in self.locks:
                if lock.locked:
                    print('The door is locked!')
                    return False
            self.opened = True
            print('You have opened the door.')
            return True

    def close_door(self) -> bool:
        if self.opened:
            self.opened = False
            print('You have closed the door.')
            return True
        else:
            print('The door is already closed.')
            return False

class Lock:
    def __init__(self) -> None:
        self.diff: int # 1 - 10
        self.material: str
        self.locked: bool
