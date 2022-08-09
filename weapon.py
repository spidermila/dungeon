from item import Item


class Weapon(Item):
    type = 'weapon'

    def __init__(
        self,
        damage: int,
        weapon_type: str,
        twohanded: bool,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.damage = damage
        self.weapon_type = weapon_type
        self.twohanded = twohanded
