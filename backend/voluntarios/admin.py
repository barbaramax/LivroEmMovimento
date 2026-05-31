from django.contrib import admin

# Register your models here.
from .models import Voluntarios, AreaInteresse

admin.site.register(Voluntarios)
admin.site.register(AreaInteresse)