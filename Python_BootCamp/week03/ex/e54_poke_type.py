import json
import requests
def poke_type(PokemonType):
    List_of_pokemon = []
    Requese_url = requests.get('https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json').json()
    List = Requese_url.get("pokemon", {})
    for i in  List :
        if ( len(PokemonType) == 1 ):
            for j in i.get("type",  {}):
                if (PokemonType[0] == j):
                    List_of_pokemon.append((i.get("id", {}), i.get("name", {})))
        else:
            if ( PokemonType == i.get("type", {})):
                    List_of_pokemon.append((i.get("id", {}), i.get("name", {})))
    print(List_of_pokemon)
    return List_of_pokemon
poke_type(["Water","Psychic"])
