from django.core.checks.messages import CheckMessage
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Card

class HomePageView(LoginRequiredMixin, ListView): 
    http_method_names = ["get"]
    template_name = "home.html"
    model = Card
    context_object_name = "cards"
    queryset = Card.objects.all().order_by('dexid')

@method_decorator(xframe_options_sameorigin, name='dispatch')
class CardDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "detail.html"
    model = Card
    context_object_name = "cards"


def ajax_change_status(request):
    dexid = request.GET.get("dexid")
    status_change = request.GET.get("status_change")
    status_value = request.GET.get("value")
    url_parameter = request.GET.get("q")
    search_filter = request.GET.get("filter")
    card_length = request.GET.get("load_limit")
    card_limit = 50



    
    # Search Bar
    if url_parameter:
        cards = Card.objects.filter(Q(poke_name__icontains=url_parameter) | Q(dexid__icontains=url_parameter))

    # Search Filters
    elif search_filter:

        search_filter_value = request.GET.get("value")

        if search_filter == "gen-filter":
            if search_filter_value == "gen1":
                cards = Card.objects.filter(generation__iexact='generation-i')
            elif search_filter_value == "gen2":
                cards = Card.objects.filter(generation__iexact='generation-ii')
            elif search_filter_value == "gen3":
                cards = Card.objects.filter(generation__iexact='generation-iii')
            elif search_filter_value == "gen4":
                cards = Card.objects.filter(generation__iexact='generation-iv')
            elif search_filter_value == "gen5":
                cards = Card.objects.filter(generation__iexact='generation-v')
            elif search_filter_value == "gen6":
                cards = Card.objects.filter(generation__iexact='generation-vi')
            elif search_filter_value == "gen7":
                cards = Card.objects.filter(generation__iexact='generation-vii')
            elif search_filter_value == "gen8":
                cards = Card.objects.filter(generation__iexact='generation-viii')
            else:
                cards = Card.objects.all()


        elif search_filter == "type-filter":
            if search_filter_value == "bug":
                cards = Card.objects.filter(Q(type1__iexact='bug') | Q(type2__iexact='bug'))
            elif search_filter_value == "dark":
                cards = Card.objects.filter(Q(type1__iexact='dark') | Q(type2__iexact='dark'))
            elif search_filter_value == "dragon":
                cards = Card.objects.filter(Q(type1__iexact='dragon') | Q(type2__iexact='dragon'))
            elif search_filter_value == "electric":
                cards = Card.objects.filter(Q(type1__iexact='electric') | Q(type2__iexact='electric'))
            elif search_filter_value == "fairy":
                cards = Card.objects.filter(Q(type1__iexact='fairy') | Q(type2__iexact='fairy'))
            elif search_filter_value == "fighting":
                cards = Card.objects.filter(Q(type1__iexact='fighting') | Q(type2__iexact='fighting'))
            elif search_filter_value == "fire":
                cards = Card.objects.filter(Q(type1__iexact='fire') | Q(type2__iexact='fire'))
            elif search_filter_value == "flying":
                cards = Card.objects.filter(Q(type1__iexact='flying') | Q(type2__iexact='flying'))
            elif search_filter_value == "ghost":
                cards = Card.objects.filter(Q(type1__iexact='ghost') | Q(type2__iexact='ghost'))
            elif search_filter_value == "grass":
                cards = Card.objects.filter(Q(type1__iexact='grass') | Q(type2__iexact='grass'))
            elif search_filter_value == "ground":
                cards = Card.objects.filter(Q(type1__iexact='ground') | Q(type2__iexact='ground'))
            elif search_filter_value == "ice":
                cards = Card.objects.filter(Q(type1__iexact='ice') | Q(type2__iexact='ice'))
            elif search_filter_value == "normal":
                cards = Card.objects.filter(Q(type1__iexact='normal') | Q(type2__iexact='normal'))
            elif search_filter_value == "poison":
                cards = Card.objects.filter(Q(type1__iexact='poison') | Q(type2__iexact='poison'))
            elif search_filter_value == "psychic":
                cards = Card.objects.filter(Q(type1__iexact='psychic') | Q(type2__iexact='psychic'))
            elif search_filter_value == "rock":
                cards = Card.objects.filter(Q(type1__iexact='rock') | Q(type2__iexact='rock'))
            elif search_filter_value == "steel":
                cards = Card.objects.filter(Q(type1__iexact='steel') | Q(type2__iexact='steel'))
            elif search_filter_value == "water":
                cards = Card.objects.filter(Q(type1__iexact='water') | Q(type2__iexact='water'))
            else:
                cards = Card.objects.all()


        elif search_filter == "gender-ratio-filter":
            if search_filter_value == "gender-neutral":
                cards = Card.objects.filter(gender_rate=-1)
            elif search_filter_value == "all-female":
                cards = Card.objects.filter(gender_rate=8)
            elif search_filter_value == "all-male":
                cards = Card.objects.filter(gender_rate=0)
            else:
                cards = Card.objects.all()


        elif search_filter == "caught-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(caught=True)
            else:
                cards = Card.objects.all()
            

        elif search_filter == "caught-shiny-filter": 
            if search_filter_value == "true":
                cards = Card.objects.filter(caught_shiny=True)
            else:
                cards = Card.objects.all()
            
        elif search_filter == "uncaught-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(caught = False)
            else:
                cards = Card.objects.all()

        elif search_filter == "uncaught-shiny-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(caught_shiny = False)
            else:
                cards = Card.objects.all()

        elif search_filter == "legendary-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(is_legendary = True)
            else:
                cards = Card.objects.all()

        elif search_filter == "mythical-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(is_mythical = True)
            else:
                cards = Card.objects.all()

        elif search_filter == "gender-diff-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(gender_differences = True)
            else:
                cards = Card.objects.all()

        elif search_filter == "ha-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(hidden_ability__isnull = False)
            else:
                cards = Card.objects.all()

        elif search_filter == "no-ha-filter":
            if search_filter_value == "true":
                cards = Card.objects.filter(hidden_ability = None)
            else:
                cards = Card.objects.all()

        elif search_filter == "pokeball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(pokeball=True) | Q(pokeball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "greatball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(greatball=True) | Q(greatball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "ultraball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(ultraball=True) | Q(ultraball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "masterball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(masterball=True) | Q(masterball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "safariball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(safariball=True) | Q(safariball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "leveball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(levelball=True) | Q(levelball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "lureball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(lureball=True) | Q(lureball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "moonball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(moonball=True) | Q(moonball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "friendball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(friendball=True) | Q(friendball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "loveball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(loveball=True) | Q(loveball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "heavyball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(heavyball=True) | Q(heavyball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "fastball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(fastball=True) | Q(fastball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "sportball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(sportball=True) | Q(sportball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "premierball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(premierball=True) | Q(premierball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "repeatball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(repeatball=True) | Q(repeatball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "timerball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(timerball=True) | Q(timerball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "nestball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(nestball=True) | Q(nestball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "netball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(netball=True) | Q(netball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "diveball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(diveball=True) | Q(diveball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "luxuryball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(luxuryball=True) | Q(luxuryball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "healball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(healball=True) | Q(healball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "quickball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(quickball=True) | Q(quickball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "duskball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(duskball=True) | Q(duskball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "cherishball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(cherishball=True) | Q(cherishball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "dreamball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(dreamball=True) | Q(dreamball_shiny=True))
            else:
                cards = Card.objects.all()

        elif search_filter == "beastball":
            if search_filter_value == "true":
                cards = Card.objects.filter(Q(beastball=True) | Q(beastball_shiny=True))
            else:
                cards = Card.objects.all()
    

    # Card information changes
    elif dexid:   
        card = Card.objects.get(pk=dexid)
        if status_value == "true":
            status_value = True
        elif status_value == "false":
            status_value = False

        # Caught status
        if status_change == "caught":
            if status_value:
                card.caught = True
                card.save()
            else:
                card.caught = False
                card.save()

        # Caught Shiny Status
        elif status_change == "caught-shiny":
            if status_value:
                card.caught_shiny = True
                card.save()
            else:
                card.caught_shiny = False
                card.save()

        # IV Changes
        
        elif status_change == "hp-iv":
            card.hp_iv = status_value
            card.save()
        elif status_change == "attack-iv":
            card.attack_iv = status_value
            card.save()
        elif status_change == "defense-iv":
            card.defense_iv = status_value
            card.save()
        elif status_change == "sp-attack-iv":
            card.sp_attack_iv = status_value
            card.save()
        elif status_change == "sp-defense-iv":
            card.sp_defense_iv = status_value
            card.save()
        elif status_change == "speed-iv":
            card.speed_iv = status_value
            card.save()

        # Nature Change
        elif status_change == "nature":
            card.nature = status_value
            card.save()

        # Ability Change
        elif status_change == "ability":
            card.ability = status_value
            card.save()

        # Ball status
        elif status_change =="pokeball":
            card.pokeball = status_value
            card.save()
        elif status_change =="greatball":
            card.greatball = status_value
            card.save()
        elif status_change =="ultraball":
            card.ultraball = status_value
            card.save()
        elif status_change =="masterball":
            card.masterball = status_value
            card.save()
        elif status_change =="premierball":
            card.premierball = status_value
            card.save()
        elif status_change =="beastball":
            card.beastball = status_value
            card.save()
        elif status_change =="cherishball":
            card.cherishball = status_value
            card.save()
        elif status_change =="dreamball":
            card.dreamball = status_value
            card.save()
        elif status_change =="safariball":
            card.safariball = status_value
            card.save()
        elif status_change =="sportball":
            card.sportball = status_value
            card.save()
        elif status_change =="diveball":
            card.diveball = status_value
            card.save()
        elif status_change =="duskball":
            card.duskball = status_value
            card.save()
        elif status_change =="healball":
            card.healball = status_value
            card.save()
        elif status_change =="luxuryball":
            card.luxuryball = status_value
            card.save()
        elif status_change =="nestball":
            card.nestball = status_value
            card.save()
        elif status_change =="netball":
            card.netball = status_value
            card.save()
        elif status_change =="quickball":
            card.quickball = status_value
            card.save()
        elif status_change =="repeatball":
            card.repeatball = status_value
            card.save()
        elif status_change =="timerball":
            card.timerball = status_value
            card.save()
        elif status_change =="fastball":
            card.fastball = status_value
            card.save()
        elif status_change =="friendball":
            card.friendball = status_value
            card.save()
        elif status_change =="heavyball":
            card.heavyball = status_value
            card.save()
        elif status_change =="levelball":
            card.levelball = status_value
            card.save()
        elif status_change =="loveball":
            card.loveball = status_value
            card.save()
        elif status_change =="lureball":
            card.lureball = status_value
            card.save()
        elif status_change =="moonball":
            card.moonball = status_value
            card.save()

        # Ball status shiny
        elif status_change =="pokeball-shiny":
            card.pokeball_shiny = status_value
            card.save()
        elif status_change =="greatball-shiny":
            card.greatball_shiny = status_value
            card.save()
        elif status_change =="ultraball-shiny":
            card.ultraball_shiny = status_value
            card.save()
        elif status_change =="masterball-shiny":
            card.masterball_shiny = status_value
            card.save()
        elif status_change =="premierball-shiny":
            card.premierball_shiny = status_value
            card.save()
        elif status_change =="beastball-shiny":
            card.beastball_shiny = status_value
            card.save()
        elif status_change =="cherishball-shiny":
            card.cherishball_shiny = status_value
            card.save()
        elif status_change =="dreamball-shiny":
            card.dreamball_shiny = status_value
            card.save()
        elif status_change =="safariball-shiny":
            card.safariball_shiny = status_value
            card.save()
        elif status_change =="sportball-shiny":
            card.sportball_shiny = status_value
            card.save()
        elif status_change =="diveball-shiny":
            card.diveball_shiny = status_value
            card.save()
        elif status_change =="duskball-shiny":
            card.duskball_shiny = status_value
            card.save()
        elif status_change =="healball-shiny":
            card.healball_shiny = status_value
            card.save()
        elif status_change =="luxuryball-shiny":
            card.luxuryball_shiny = status_value
            card.save()
        elif status_change =="nestball-shiny":
            card.nestball_shiny = status_value
            card.save()
        elif status_change =="netball-shiny":
            card.netball_shiny = status_value
            card.save()
        elif status_change =="quickball-shiny":
            card.quickball_shiny = status_value
            card.save()
        elif status_change =="repeatball-shiny":
            card.repeatball_shiny = status_value
            card.save()
        elif status_change =="timerball-shiny":
            card.timerball_shiny = status_value
            card.save()
        elif status_change =="fastball-shiny":
            card.fastball_shiny = status_value
            card.save()
        elif status_change =="friendball-shiny":
            card.friendball_shiny = status_value
            card.save()
        elif status_change =="heavyball-shiny":
            card.heavyball_shiny = status_value
            card.save()
        elif status_change =="levelball-shiny":
            card.levelball_shiny = status_value
            card.save()
        elif status_change =="loveball-shiny":
            card.loveball_shiny = status_value
            card.save()
        elif status_change =="lureball-shiny":
            card.lureball_shiny = status_value
            card.save()
        elif status_change =="moonball-shiny":
            card.moonball_shiny = status_value
            card.save()

    # For future implementation
    # elif card_length: 

    #     if int(card_length) <= card_limit:
    #         card_limit += card_limit
    #     cards = Card.objects[0:card_limit]

    else:
        cards = Card.objects[0:card_limit]


    if request.is_ajax():
        html = render_to_string(
            template_name="search-results-partial.html",
            context={"cards": cards}
        )

        data_dict = {"html_from_view" : html}
        return JsonResponse(data=data_dict, safe=False)
