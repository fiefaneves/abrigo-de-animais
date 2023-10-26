from django.db import models

# Create your models here.
class Adocoes(models.Model):
    especies = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Coelho', 'Coelho'),
        ('Tartaruga', 'Tartaruga'),
        ('Hamster', 'Hamster')
    )
    foto = models.ImageField(upload_to="fotos_pets", default='fotos_pets/', null=True, blank=True)
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, choices=especies)
    idade = models.IntegerField()
    raca = models.CharField(max_length=50)
    historico_de_saude = models.TextField()
    data_de_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome}: {self.especie} - {self.idade} - {self.raca}'
    
    class Meta:
        verbose_name = 'Cadastro de animal'
        verbose_name_plural = 'Cadastros de animais'
        ordering = ['nome']