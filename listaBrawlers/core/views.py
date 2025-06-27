from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Musicas

# Create your views here.
def listaMusicas(request):
    musicas = Musicas.objects.all()
    #o metodo all seria equivalente ao "SELECT * do sql"
    context = {
        'musicas': musicas
    }
    return render(request, 'index.html', context)


def detalheMusica(request, pk):
    # pk é o id da musica que vai se clicada
    musica = get_object_or_404(Musicas, pk=pk)
    # get_object_or_404 vai tentar pegar o objeto caso ele não exista retorna o erro 404
    return render(request, 'detalheMusica.html', {'musica': musica})
    
