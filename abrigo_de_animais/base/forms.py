from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.IntegerField()
    senha = forms.CharField(widget=forms.PasswordInput)