from django.urls import path
from adocoes.views import escolha_seu_amigo

app_name = 'Adoções'
urlpatterns = [
    path('escolha_amigo/', escolha_seu_amigo, name='escolha_seu_amigo')
]