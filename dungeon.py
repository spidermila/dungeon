from typing import List


class Player:
    def __init__(self) -> None:
        self.name = ''
        self.items: List[Item] = []


class Room:
    def __init__(self, id: int) -> None:
        self.id = id
        self.items: List[Item] = []
        self.connections: List[int] = []
        self.description = ''

    def connect_to(self, room_ids: list) -> None:
        for r in room_ids:
            self.connections.append(r)


class Dungeon:
    def __init__(self) -> None:
        self.rooms: List[Room] = []

    def create_room(self) -> None:
        if len(self.rooms) == 0:
            self.rooms.append(Room(0))


class Item:
    type = 'item'
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

class Clothes(Item):
    type = 'clothes'
    def __init__(self, color: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.wearable = True

def main():
    p = Player()
    p.items.append(Item(name = 'neco', weight = 1))
    p.items.append(Clothes(name = 'shirt', weight = 1, color = 'red'))


if __name__ == '__main__':
    exit(main())
