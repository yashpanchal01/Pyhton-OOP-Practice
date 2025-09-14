# How to connect to an API using Python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(Name):
    URL = f"{base_url}/pokemon/{Name}"
    response = requests.get(URL)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else: 
        print("Failed to Retrive DATA!")
    

pokemon_Name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_Name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"Weight: {pokemon_info["weight"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"id: {pokemon_info["id"]}")


# print and return are not the same, Both have different use cases. 

# if somethinge goes wrong like you forgot putting parenthesis after something,
# it wont be interpreted as error for some reason. and you will wonder whats causeing error.