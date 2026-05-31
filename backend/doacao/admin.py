from django.contrib import admin

from .models import Doacao

# Register your models here.
admin.site.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'quantidade_livros', 'criado_em')
    search_fields = ('nome', 'email')
    list_filter = ('criado_em',)