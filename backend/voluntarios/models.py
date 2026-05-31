from django.db import models

# Create your models here.
class AreaInteresse(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Voluntarios(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    area_interesse = models.ManyToManyField(AreaInteresse)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Voluntário"
        verbose_name_plural = "Voluntários"