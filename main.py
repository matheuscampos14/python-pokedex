from pokeapi import search_pokemon
"""
Python Pokédex

First version:
- Consume PokéAPI
- Display Pokémon information
"""

pokemon = input("Digite o nome do Pokémon: ")
data = search_pokemon(pokemon)

print(f"Nome: {data['name'].capitalize()}")
print(f"ID: {data['id']}")
types = []
for tipo in data["types"]:
    types.append(tipo["type"]["name"].capitalize())
print("Tipo(s): " + ", ".join(types))
print(f"Altura: {data['height']/10} m")
print(f"Peso: {data['weight']/10} kg")

print(f"\nHabilidades: ")
for ability in data['abilities']:
    print(f"- {ability['ability']['name'].capitalize()}")

print(f'\nSprite:\n{data["sprites"]["front_default"]}')
print(f"\nCry:\n{data['cries']['latest']}")
