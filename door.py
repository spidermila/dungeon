from typing import Any
from typing import List

class Door:
    def __init__(self, room: Any) -> None:
        self.room = room
        self.direction: str = ''
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
    def __init__(self, material: str, locked: bool, diff: int = 1) -> None:
        self.diff = diff # 1 - 10
        self.material = material
        self.locked = locked
