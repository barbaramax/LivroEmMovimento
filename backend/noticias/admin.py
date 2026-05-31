from django.contrib import admin

from .models import Evento, Noticia

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'local')

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criado_em')
    search_fields = ('titulo',)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Noticia, NoticiaAdmin)