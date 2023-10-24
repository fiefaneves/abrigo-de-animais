from django.contrib import admin
from adocoes.models import Adocoes

# Register your models here.
@admin.register(Adocoes)
class AdocoesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'especie', 'idade', 'raca', 'data_de_cadastro']
    search_field = ['nome', 'especie', 'raca']
    list_filter = ['data_de_cadastro']