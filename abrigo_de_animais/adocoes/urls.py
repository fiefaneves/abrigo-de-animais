from django.urls import path
from adocoes.views import cadastro_adocao, amigos_disponiveis

app_name = 'Adoções'
urlpatterns = [
    path('cadastro_amigo/', cadastro_adocao, name='cadastro_amigo'),
    path('amigos_disponiveis/', amigos_disponiveis, name='escolha_seu_amigo')
]