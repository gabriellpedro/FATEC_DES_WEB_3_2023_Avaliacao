from django import forms
from .models import Presenca

class PresencaForm(forms.ModelForm):
    class Meta: 
        model = Presenca
        fields = '__all__'