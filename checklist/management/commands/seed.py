import requests
from django.core.management.base import BaseCommand
from ...models import Card


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
    pokeinfo = []

    for i in get_data():
        response = requests.get(i)
        data = response.json()
        pokeinfo.append(data)

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

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_cards()
        # clear_data()
        print("Pokemon data seed complete!")
