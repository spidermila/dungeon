from typing import List

from item import Item

class Room:
    def __init__(self, id: int, description: str) -> None:
        self.id = id
        self.items: List[Item] = []
        self.connections: List[int] = []
        self.description = description

    def connect_to(self, room_ids: list) -> None:
        for r in room_ids:
            self.connections.append(r)
