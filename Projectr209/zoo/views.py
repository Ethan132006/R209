from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Zoo, Animal
from .forms import ZooForm, AnimalForm

# ZOO CRUD
class ZooListView(ListView):
    model = Zoo
    template_name = 'zoo/zoo_list.html'

class ZooDetailView(DetailView):
    model = Zoo
    template_name = 'zoo/zoo_detail.html'

class ZooCreateView(CreateView):
    model = Zoo
    form_class = ZooForm
    template_name = 'zoo/zoo_form.html'
    success_url = reverse_lazy('zoo_list')

class ZooUpdateView(UpdateView):
    model = Zoo
    form_class = ZooForm
    template_name = 'zoo/zoo_form.html'
    success_url = reverse_lazy('zoo_list')

class ZooDeleteView(DeleteView):
    model = Zoo
    template_name = 'zoo/zoo_confirm_delete.html'
    success_url = reverse_lazy('zoo_list')


# ANIMAL CRUD
class AnimalListView(ListView):
    model = Animal
    template_name = 'zoo/animal_list.html'

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'zoo/animal_detail.html'

class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'zoo/animal_form.html'
    success_url = reverse_lazy('animal_list')

class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'zoo/animal_form.html'
    success_url = reverse_lazy('animal_list')

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'zoo/animal_confirm_delete.html'
    success_url = reverse_lazy('animal_list')


