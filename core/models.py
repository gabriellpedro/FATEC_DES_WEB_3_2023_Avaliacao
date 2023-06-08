from django.db import models

class Presenca(models.Model):
    NomeAluno = models.CharField(verbose_name="Nome do Aluno", max_length=100)
    NomeProfessor = models.CharField(verbose_name="Nome do Professor", max_length=100)
    Semestre = models.IntegerField(verbose_name="Semestre")
    NomeCurso = models.CharField(verbose_name="Nome do Curso", max_length=20)
    DataPresenca = models.DateField(verbose_name="Data de Presença")
    
