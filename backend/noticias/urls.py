from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='eventos'),
    path('api/', views.noticias_api, name='noticias_api'),
]