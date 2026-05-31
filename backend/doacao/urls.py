from django.urls import path
from . import views

urlpatterns = [
    path('', views.receber_doacao, name='receber_doacao'),
]