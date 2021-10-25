from django.urls import path
from checklist import views
from django.conf.urls import url

app_name = "checklist"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path('card/<int:pk>/', views.CardDetailView.as_view(), name="detail"),
    url(r'^ajax/change_status/$', views.ajax_change_status, name="ajax_change_status")
]