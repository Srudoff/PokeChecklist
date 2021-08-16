from django.views.generic import ListView, DetailView
from .models import Card

class HomePageView(ListView): 
    http_method_names = ["get"]
    template_name = "home.html"
    model = Card
    context_object_name = "cards"
    queryset = Card.objects.all().order_by('dexid')

class CardDetailView(DetailView):
    template_name = "detail.html"
    model = Card