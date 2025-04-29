from django import forms
from .models import Zoo, Animal

class ZooForm(forms.ModelForm):
    class Meta:
        model = Zoo
        fields = ['nom', 'ville', 'superficie', 'directeur_du_zoo','date_de_creation']


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nom', 'espece', 'age', 'zoo','date_naissance']


