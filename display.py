def show_pokemon(data):
    print(f"Nome: {data.name}")
    print(f"ID: {data.pokemon_id}")

    print("Tipo(s): " + ", ".join(data.types))
    print(f"Altura: {data.height} m")
    print(f"Peso: {data.weight} kg")

    print(f"\nHabilidades: ")
    for ability in data.abilities:
        print(f"- {ability}")

    print(f'\nSprite:\n{data.sprite}')
    print(f"\nCry:\n{data.cry}")