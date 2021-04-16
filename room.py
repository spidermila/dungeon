from typing import List

from item import Item

class Room:
    def __init__(self, description: str) -> None:
        self.items: List[Item] = []
        self.connections: List[int] = []
        self.description = description
        self.doors: List[int] = []
        self.location: List[int] = []

    def connect_to(self, room_ids: list) -> None:
        for r in room_ids:
            self.connections.append(r)
