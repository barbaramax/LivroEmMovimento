from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_evento = models.DateTimeField()
    local = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='eventos/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-data_evento']

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-criado_em']