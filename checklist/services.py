# from checklist.models import Card
import requests
from .models import Card

def get_data():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1118&offset=0'
    response = requests.get(url)
    data = response.json()
    pokemon = data['results']
    poke_urls = []

    for i in pokemon:
        
        poke_urls.append(i['url'])

    return poke_urls

def get_cards():

    for i in get_data():
        response = requests.get(i)
        pokeinfo = response.json()

    return pokeinfo

def seed_cards():
    for i in get_cards():
        pokemon_data = Card(
            poke_name = i['name'],
            dexid = i['id'],
        )

        pokemon_data.save()

def clear_data():
    Card.objects.all().delete()














# v1:
# primary type
# secondary type
# generation
# gender ratio
# legendary
# mythical
# caught
# caught shiny
# ball types? (bool?)
# sprites/pics
# alt forms/is_default
# family/evos

# if evolves_from_species == this - 1:
#     blah blah blah







# v2:
# egg groups
# obtainable/unobtainable gen8
# no hidden ability
# mega evo
# gigantamax
# stats
