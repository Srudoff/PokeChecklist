import requests
from django.core.management.base import BaseCommand
from ...models import Card

pokeball_sprites = []
pokeinfo = []
speciesinfo = []
pokemon_data = []

def get_data():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1118&offset=0'
    response = requests.get(url)
    data = response.json()
    pokemon = data['results']
    poke_urls = []

    for i in pokemon:
        
        poke_urls.append(i['url'])

    return poke_urls

def get_pokeball_sprites():
    urls = ['https://pokeapi.co/api/v2/item-category/33/', 'https://pokeapi.co/api/v2/item-category/34/', 'https://pokeapi.co/api/v2/item-category/39/']

    for i in urls:
        response = requests.get(i)
        data = response.json()
        for j in data['items']:
            r = requests.get(j['url'])
            sprite = r.json()
            pokeball_sprites.append(sprite['sprites']['default'])
            pokeball_sprites.append(sprite['name'])
   
    return pokeball_sprites

def get_poke_info():

    for i in get_data():
        response = requests.get(i)
        data = response.json()
        pokeinfo.append(data)

    return pokeinfo

def get_species_info():

    for i in get_poke_info():
        response = requests.get(i['species']['url'])
        data = response.json()
        speciesinfo.append(data)

    pokemon_data = list(zip(pokeinfo, speciesinfo))

    return pokemon_data

def seed_cards():
    # Use i[0] to get information from pokeinfo
    # Use i[1] to get information from speciesinfo

    pokeball_sprites = get_pokeball_sprites()

    for i in get_species_info():

        if len(i[0]['types']) > 1:
            type2 = i[0]['types'][1]['type']['name']
        else: 
            type2 = None

        for ability in i[0]['abilities']:
            if ability['slot'] == 2:
                ability2 = ability['ability']['name']
            else:
                ability2 = None

            if ability['is_hidden']:
                hidden_ability = ability['ability']['name']
            else: 
                hidden_ability = None

        if i[1]['evolves_from_species'] is not None:
            evolves_from_species = i[1]['evolves_from_species']['name']
        else:
            evolves_from_species = None


        pokemon_data = Card(
            poke_name = i[0]['species']['name'],
            dexid = i[0]['id'],
            image = i[0]['sprites']['other']['official-artwork']['front_default'],
            poke_sprite = i[0]['sprites']['front_default'],
            shiny_sprite = i[0]['sprites']['front_shiny'],
            type1 = i[0]['types'][0]['type']['name'],
            type2 = type2,
            is_default = i[0]['is_default'],
            ability1 = i[0]['abilities'][0]['ability']['name'],
            ability2 = ability2,
            hidden_ability = hidden_ability,
            generation = i[1]['generation']['name'],
            evolves_from_species = evolves_from_species,
            is_legendary = i[1]['is_legendary'],
            is_mythical = i[1]['is_mythical'],
            gender_rate = i[1]['gender_rate'],
            gender_differences = i[1]['has_gender_differences'],
            caught = False,
            caught_shiny = False,
            pokeball = False,
            pokeball_img = pokeball_sprites[pokeball_sprites.index("poke-ball") - 1],
            greatball = False,
            greatball_img = pokeball_sprites[pokeball_sprites.index("great-ball") - 1],
            ultraball = False,
            ultraball_img = pokeball_sprites[pokeball_sprites.index("ultra-ball") - 1],
            masterball = False,
            masterball_img = pokeball_sprites[pokeball_sprites.index("master-ball") - 1],
            safariball = False,
            safariball_img = pokeball_sprites[pokeball_sprites.index("safari-ball") - 1],
            levelball = False,
            levelball_img = pokeball_sprites[pokeball_sprites.index("level-ball") - 1],
            lureball = False,
            lureball_img = pokeball_sprites[pokeball_sprites.index("lure-ball") - 1],
            moonball = False,
            moonball_img = pokeball_sprites[pokeball_sprites.index("moon-ball") - 1],
            friendball = False,
            friendball_img = pokeball_sprites[pokeball_sprites.index("friend-ball") - 1],
            loveball = False,
            loveball_img = pokeball_sprites[pokeball_sprites.index("love-ball") - 1],
            heavyball = False,
            heavyball_img = pokeball_sprites[pokeball_sprites.index("heavy-ball") - 1],
            fastball = False,
            fastball_img = pokeball_sprites[pokeball_sprites.index("fast-ball") - 1],
            sportball = False,
            sportball_img = pokeball_sprites[pokeball_sprites.index("sport-ball") - 1],
            premierball = False,
            premierball_img = pokeball_sprites[pokeball_sprites.index("premier-ball") - 1],
            repeatball = False,
            repeatball_img = pokeball_sprites[pokeball_sprites.index("repeat-ball") - 1],
            timerball = False,
            timerball_img = pokeball_sprites[pokeball_sprites.index("timer-ball") - 1],
            nestball = False,
            nestball_img = pokeball_sprites[pokeball_sprites.index("nest-ball") - 1],
            netball = False,
            netball_img = pokeball_sprites[pokeball_sprites.index("net-ball") - 1],
            diveball = False,
            diveball_img = pokeball_sprites[pokeball_sprites.index("dive-ball") - 1],
            luxuryball = False,
            luxuryball_img = pokeball_sprites[pokeball_sprites.index("luxury-ball") - 1],
            healball = False,
            healball_img = pokeball_sprites[pokeball_sprites.index("heal-ball") - 1],
            quickball = False,
            quickball_img = pokeball_sprites[pokeball_sprites.index("quick-ball") - 1],
            duskball = False,
            duskball_img = pokeball_sprites[pokeball_sprites.index("dusk-ball") - 1],
            cherishball = False,
            cherishball_img = pokeball_sprites[pokeball_sprites.index("cherish-ball") - 1],
            dreamball = False,
            dreamball_img = pokeball_sprites[pokeball_sprites.index("dream-ball") - 1],
            beastball = False,
            beastball_img = pokeball_sprites[pokeball_sprites.index("beast-ball") - 1],
        )
        pokemon_data.save()

def clear_data():
    Card.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_cards()
        # clear_data()
        print("Pokemon data seed complete!")
