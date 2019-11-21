import json
import requests
def poke_gallery(String):
    pokemon_collection = open('pokemon.html', 'w')
    Requese_url = requests.get('https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json').json()
    List = Requese_url.get("pokemon", {})
    if(len(String) == 0):
        for i in List:
                pokemon_collection.write('<img src="{}" height="100px" width="100px"> '.format(i.get("img", {})))
        pokemon_collection.close()
    elif( len(String) == 1 ):
        for i in List:
            for j in i.get("type", {}):
                if ( String[0] == j):
                   pokemon_collection.write('<img src="{}" height="100px" width="100px"> '.format(i.get("img", {})))
    else:
        for i in List:
                if ( String == i.get("type", {})):
                   pokemon_collection.write('<img src="{}" height="100px" width="100px"> '.format(i.get("img", {})))
poke_gallery(["Water","Psychic"])
