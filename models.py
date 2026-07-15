class Pokemon:
    def __init__(self, name, pokemon_id, types, height, weight, abilities, sprite, cry):
        self.name = name
        self.pokemon_id = pokemon_id
        self.types = types
        self.height = height
        self.weight = weight
        self.abilities = abilities
        self.sprite = sprite
        self.cry = cry

    @classmethod
    def from_api_response(cls,data):
        types = []

        for pokemon_type in data["types"]:
            types.append(
                pokemon_type["type"]["name"].capitalize()
            )

        abilities = []

        for ability in data["abilities"]:
            abilities.append(
                ability["ability"]["name"].capitalize()
            )

        return cls(
            name=data["name"].capitalize(),
            pokemon_id=data["id"],
            types=types,
            height=data["height"] / 10,
            weight=data["weight"] / 10,
            abilities=abilities,
            sprite=data["sprites"]["front_default"],
            cry=data["cries"]["latest"]
        )