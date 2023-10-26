from django.shortcuts import render
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

def detalhes(request):
    adocoes = Adocoes.objects.all()
    contexto = {
        'adocoes': adocoes
    }
    return render(request, 'detalhes.html', contexto)