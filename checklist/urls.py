from django.urls import path
from django.urls.resolvers import URLPattern
from checklist import views

app_name = "checklist"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path('card/<int:id>/', views.CardDetailView.as_view(), name="detail"),
]