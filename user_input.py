def get_user_input():
    pokemon_name = input("> Enter the name of the Pokémon: ")
    if not pokemon_name.strip():
        print("Invalid input! Please enter a valid Pokémon name.")
        return get_user_input()
    return pokemon_name.strip().lower()