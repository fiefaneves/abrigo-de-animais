from django import forms
from adocoes.models import Adocoes

class AdocoesForm(forms.ModelForm):
    class Meta:
        model = Adocoes
        fields = ['nome', 'especie', 'idade', 'raca', 'historico_de_saude' ]