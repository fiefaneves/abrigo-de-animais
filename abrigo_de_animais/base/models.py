from django.db import models
from adocoes.models import Adocoes
# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(Adocoes, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, default=None)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['-data']
