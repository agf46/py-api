import requests 
import json 
import pprint

API_CALL = "https://pokeapi.co/api/v2/generation/generation-ii"
# The below call will just give you a response code 
# requests.get(API_CALL)

# Get pokemon in json 
results = requests.get(API_CALL)
results.json()  # Returns a json dict 

data = results.json()
data['pokemon_species']
pprint.pprint(data)