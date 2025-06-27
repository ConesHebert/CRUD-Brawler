from django.shortcuts import render
from .models import Musicas

# Create your views here.
def lista_musicas(request):
    musicas = Musicas.objects.all()
    #o metodo all seria equivalente ao "SELECT * do sql"
    context = {
        'musicas': musicas
    }
    return render(request, 'index.html', context)

