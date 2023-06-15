from django import forms
from .models import Presenca

class PresencaForm(forms.ModelForm):
    class Meta: 
        model = Presenca
        fields = '__all__'

    def clean_NomeAluno(self):
        NomeAluno = self.cleaned_data['NomeAluno']
        return NomeAluno
    
    def clean_NomeProfessor(self):
        NomeProfessor = self.cleaned_data['NomeProfessor']
        return NomeProfessor

    def clean_Semestre(self): 
        Semestre = self.cleaned_data['Semestre']
        return Semestre
    
    def clean_NomeCurso(self):   
        NomeCurso = self.cleaned_data['NomeCurso']
        return NomeCurso
    
    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data