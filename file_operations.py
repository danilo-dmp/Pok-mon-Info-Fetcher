from datetime import datetime
import json

def save_to_file(data, pokemon_name):
    data_str = datetime.now().strftime("%m-%d-%Y")
    filename = f"{pokemon_name}_data_{data_str}.txt"

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    return filename