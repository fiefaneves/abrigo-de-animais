from django.shortcuts import render
from base.forms import CadastroForm
from adocoes.models import Adocoes

# Create your views here.
def inicio(request):
    adocoes = Adocoes.objects.all()
    contexto = {
        'adocoes': adocoes
    }
    return render(request, 'inicio.html', contexto)

def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)