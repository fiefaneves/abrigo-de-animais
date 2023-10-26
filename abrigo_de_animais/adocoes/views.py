from django.shortcuts import render, get_object_or_404
from adocoes.forms import AdocoesForm
from adocoes.models import Adocoes
from django.views.decorators.cache import cache_page

# Create your views here.
def cadastro_adocao(request):
    print (request.FILES)
    form = AdocoesForm(request.POST or None, request.FILES or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro_amigo.html', contexto)

def amigos_disponiveis(request):
    adocoes = Adocoes.objects.all()
    contexto = {
        'adocoes': adocoes
    }
    return render(request, 'amigos_disponiveis.html', contexto)

def detalhes_animal(request, animal_id):
    animal = get_object_or_404(Adocoes, pk=animal_id)
    contexto = {
        'animal': animal
    }
    return render(request, 'detalhes_animal.html', contexto)