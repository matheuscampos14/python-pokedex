import requests

def search_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise ValueError(f"Pokémon não encontrado")

    return response.json()