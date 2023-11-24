from django.urls import path
from adocoes.views import cadastro_adocao, amigos_disponiveis, detalhes_animal, busca

app_name = 'Adoções'
urlpatterns = [
    path('cadastro_amigo/', cadastro_adocao, name='cadastro_amigo'),
    path('amigos_disponiveis/', amigos_disponiveis, name='escolha_seu_amigo'),
    path('amigo/<int:animal_id>/', detalhes_animal, name='detalhes_animal'),
    path('resultados_busca/', busca, name='resultados_busca.html')
]