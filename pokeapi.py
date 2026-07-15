import requests

def search_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise ValueError(
            f"Erro {response.status_code}: não foi possível obter os dados do Pokémon."
        )

    return response.json()