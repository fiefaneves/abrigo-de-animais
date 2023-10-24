from django.shortcuts import render
from adocoes.models import Adocoes

# Create your views here.
def escolha_seu_amigo(request):
    return render(request, 'escolha_amigo.html')