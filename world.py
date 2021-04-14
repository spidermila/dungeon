from typing import List

from room import Room
class World:
    def __init__(self) -> None:
        self.rooms: List[Room] = []
