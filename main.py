import requests

#pokemon = input("Digite o nome do Pokémon: ")
pokemon = 'Charizard'

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url)
if response.status_code != 200:
    raise ValueError(
        f"Erro {response.status_code}: não foi possível obter os dados do Pokémon."
    )

dados = response.json()

print(f"Nome: {dados['name'].capitalize()}")
print(f"ID: {dados['id']}")
types = []
for tipo in dados["types"]:
    types.append(tipo["type"]["name"].capitalize())
print("Tipo(s): " + ", ".join(types))
print(f"Altura: {dados['height']/10} m")
print(f"Peso: {dados['weight']/10} kg")

print(f"\nHabilidades: ")
for ability in dados['abilities']:
    print(f"- {ability['ability']['name'].capitalize()}")

print(f'Sprite:\n{dados["sprites"]["front_default"]}')
print(f"\nCry:\n{dados['cries']['latest']}")
