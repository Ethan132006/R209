from django.urls import path
from . import views

urlpatterns = [

    # ZOO URLs
    path('zoos/', views.ZooListView.as_view(), name='zoo_list'),
    path('zoos/<int:pk>/', views.ZooDetailView.as_view(), name='zoo_detail'),
    path('zoos/add/', views.ZooCreateView.as_view(), name='zoo_add'),
    path('zoos/<int:pk>/edit/', views.ZooUpdateView.as_view(), name='zoo_edit'),
    path('zoos/<int:pk>/delete/', views.ZooDeleteView.as_view(), name='zoo_delete'),

    # ANIMAL URLs
    path('animaux/', views.AnimalListView.as_view(), name='animal_list'),
    path('animaux/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('animaux/add/', views.AnimalCreateView.as_view(), name='animal_add'),
    path('animaux/<int:pk>/edit/', views.AnimalUpdateView.as_view(), name='animal_edit'),
    path('animaux/<int:pk>/delete/', views.AnimalDeleteView.as_view(), name='animal_delete'),

]



