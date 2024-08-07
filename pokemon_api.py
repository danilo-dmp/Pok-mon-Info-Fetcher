import json
import requests

def fetch_pokemon_data(pokemon_name):
    base_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {pokemon_name}. Try again.")
        return None