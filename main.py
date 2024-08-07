from user_input import get_user_input
from pokemon_api import fetch_pokemon_data
from file_operations import save_to_file
from email_operations import send_email_with_attachment

def main():
    pokemon_name = get_user_input()

    pokemon_data = fetch_pokemon_data(pokemon_name)
    if pokemon_data:
        filename = save_to_file(pokemon_data, pokemon_name)
        send_email_with_attachment("RECIPIENT EMAIL (CHANGE)", "Pokémon Data", f"Here is the data for {pokemon_name} attached.", filename)

if __name__ == "__main__":
    main()