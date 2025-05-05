from django.urls import path
from . import views

urlpatterns = [
    path('', views.zoo_list, name='zoo_list'),
    path('zoo/<int:pk>/', views.zoo_detail, name='zoo_detail'),
    path('zoo/create/', views.zoo_create, name='zoo_create'),
    path('zoo/<int:pk>/edit/', views.zoo_update, name='zoo_update'),
    path('zoo/<int:pk>/delete/', views.zoo_delete, name='zoo_delete'),
    path('zoo/<int:zoo_id>/animal/create/', views.animal_create, name='animal_create'),
    path('animal/<int:pk>/edit/', views.animal_update, name='animal_update'),
    path('animal/<int:pk>/delete/', views.animal_delete, name='animal_delete'),
]





