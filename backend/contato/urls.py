from django.urls import path

from . import views

app_name = "contato"

urlpatterns = [
    path("", views.pagina_teste, name="teste"),
    path("email/", views.email_redirect, name="email"),
    path("whatsapp/", views.whatsapp_redirect, name="whatsapp"),
    path("info/", views.contact_info, name="info"),
]
