# Generated by Django 4.2.2 on 2023-06-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomeAluno', models.CharField(max_length=100, verbose_name='Nome do Aluno')),
                ('NomeProfessor', models.CharField(max_length=100, verbose_name='Nome do Professor')),
                ('Semestre', models.IntegerField(verbose_name='Semestre')),
                ('NomeCurso', models.CharField(max_length=20, verbose_name='Nome do Curso')),
                ('DataPresenca', models.DateField(verbose_name='Data de Presença')),
            ],
        ),
    ]
