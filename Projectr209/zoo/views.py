from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Zoo, Animal
from .forms import ZooForm, AnimalForm

def zoo_list(request):
    zoos = Zoo.objects.all()
    return render(request, 'zoo/zoo_list.html', {'zoos': zoos})

def zoo_detail(request, pk):
    zoo = get_object_or_404(Zoo, pk=pk)
    return render(request, 'zoo/zoo_detail.html', {'zoo': zoo})

def zoo_create(request):
    form = ZooForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('zoo_list')
    return render(request, 'zoo/zoo_form.html', {'form': form})

def zoo_update(request, pk):
    zoo = get_object_or_404(Zoo, pk=pk)
    form = ZooForm(request.POST or None, instance=zoo)
    if form.is_valid():
        form.save()
        return redirect('zoo_detail', pk=pk)
    return render(request, 'zoo/zoo_form.html', {'form': form})

def zoo_delete(request, pk):
    zoo = get_object_or_404(Zoo, pk=pk)
    if request.method == 'POST':
        zoo.delete()
        return redirect('zoo_list')
    return render(request, 'zoo/zoo_confirm_delete.html', {'zoo': zoo})

def animal_create(request, zoo_id):
    zoo = get_object_or_404(Zoo, pk=zoo_id)
    form = AnimalForm(request.POST or None, initial={'zoo': zoo})
    if form.is_valid():
        form.save()
        return redirect('zoo_detail', pk=zoo_id)
    return render(request, 'zoo/animal_form.html', {'form': form, 'zoo': zoo})

def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    form = AnimalForm(request.POST or None, instance=animal)
    if form.is_valid():
        form.save()
        return redirect('zoo_detail', pk=animal.zoo.pk)
    return render(request, 'zoo/animal_form.html', {'form': form})

def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        zoo_id = animal.zoo.pk
        animal.delete()
        return redirect('zoo_detail', pk=zoo_id)
    return render(request, 'zoo/animal_confirm_delete.html', {'animal': animal})








































