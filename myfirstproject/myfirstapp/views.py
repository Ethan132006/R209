from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"myfirstapp/index.html")

def formulaire(request):
    return render(request,"myfirstapp/formulaire.html")

def bonjour(request):
    return render(request,"myfirstapp/bonjour.html")

