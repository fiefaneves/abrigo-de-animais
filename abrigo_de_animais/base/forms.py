from django import forms
from base.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'telefone', 'pet']
        widgets = {'senha': forms.PasswordInput()}