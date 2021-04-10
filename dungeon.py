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
    def __init__(self, properties: dict) -> None:
        self.name = properties['name']
        self.type = properties['type']
        self.weight = properties['weight']


def main():
    p = Player()
    p.items.append(
        Item({
            'name': 'Hat',
            'type': 'clothes',
            'weight': 1,
        }),
    )


if __name__ == '__main__':
    exit(main())
