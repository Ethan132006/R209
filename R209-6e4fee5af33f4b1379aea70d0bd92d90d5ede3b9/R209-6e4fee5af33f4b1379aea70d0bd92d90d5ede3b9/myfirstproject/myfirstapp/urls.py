from django.urls import path
from . import views  # Assure-toi d'avoir les vues dans views.py

urlpatterns = [
    path('', views.index, name='index'),  # Route pour "index"
    path('bonjour/', views.bonjour, name='bonjour'),  # Route pour "bonjour"
]
