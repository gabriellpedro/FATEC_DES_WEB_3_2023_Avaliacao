from django.db import models

from core.enums import CURSOS, PROFESSORES, SEMESTRES

class Presenca(models.Model):
    NomeAluno = models.CharField(verbose_name="Nome_do_Aluno", max_length=100)
    NomeProfessor = models.IntegerField(verbose_name='Nome_do_Professor', choices=PROFESSORES)
    Semestre = models.IntegerField(verbose_name="Semestre", choices=SEMESTRES)
    NomeCurso = models.IntegerField(verbose_name='Nome_do_Curso', choices=CURSOS)
    
