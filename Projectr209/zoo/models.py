from django.db import models
import datetime  # Nécessaire pour les valeurs par défaut des dates


class Zoo(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    superficie = models.FloatField(help_text="Superficie en m²", blank=True, null=True)
    directeur_du_zoo = models.CharField(max_length=100, blank=True, null=True)
    date_de_creation = models.DateField(blank=True , null=True)  # Meilleure pratique

    def __str__(self):
        return self.nom


class Animal(models.Model):
    nom = models.CharField(max_length=100)
    espece = models.CharField(max_length=100)
    age = models.IntegerField(blank=True , null=True)
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE, related_name='animaux')
    date_naissance = models.DateField(blank=True , null=True)

    def __str__(self):
        return f"{self.nom} ({self.espece})"
