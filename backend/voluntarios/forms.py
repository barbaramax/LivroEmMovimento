from django import forms
from .models import Voluntarios

class VoluntariosForm(forms.ModelForm):
    class Meta:
        model = Voluntarios
        fields = ['nome', 'email', 'telefone', 'area_interesse']