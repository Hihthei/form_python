import json
import os
from pathlib import Path
from src.forma_fun.forma_func import list_main_ui

chemin_json = Path(__file__).resolve().parents[3] / 'data_list' / 'grocery_list' / 'grocery_data.json'

grocery_list = None

if not chemin_json.exists():
    print("fichier inexistant")

    with open(chemin_json, 'w') as file:
        json.dump("", file, indent=4)
else:
    grocery_list = json.load(open(chemin_json))

grocery_list = list_main_ui(grocery_list)

with open(chemin_json, 'w') as file:
    json.dump(grocery_list, file, indent=4)
