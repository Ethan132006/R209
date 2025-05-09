# Generated by Django 5.2 on 2025-04-29 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zoo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('superficie', models.FloatField(blank=True, help_text='Superficie en m²', null=True)),
                ('directeur_du_zoo', models.CharField(blank=True, max_length=100, null=True)),
                ('date_de_creation', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('espece', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('zoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animaux', to='zoo.zoo')),
            ],
        ),
    ]
