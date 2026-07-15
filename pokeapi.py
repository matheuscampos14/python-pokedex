from models import Pokemon
import requests

def search_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise ValueError(f"Pokémon não encontrado")

    return Pokemon.from_api_response(response.json())