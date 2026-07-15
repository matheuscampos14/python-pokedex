from pokeapi import search_pokemon
from display import show_pokemon
"""
Python Pokédex

First version:
- Consume PokéAPI
- Display Pokémon information
"""

pokemon = input("Digite o nome do Pokémon: ")

try:
    data = search_pokemon(pokemon)
except ValueError:
    print("Pokémon não encontrado.")
    exit()

show_pokemon(data)