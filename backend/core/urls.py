from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('', views.home),
]