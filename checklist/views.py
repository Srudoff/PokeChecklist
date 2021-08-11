from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Card
import requests

class HomePageView(TemplateView):
    http_method_names = ["get"]
    template_name = "home.html"
    model = Card
    context_object_name = "cards"
    queryset = Card.objects.all().order_by('dexid')

class CardDetailView(DetailView):
    template_name = "detail.html"
    model = Card


def get_cards(request):
    all_cards = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://pokeapi.co/api/v2/pokemon/' % name
        response = requests.get(url)
        data = response.json()
        pokemon = data['name']
