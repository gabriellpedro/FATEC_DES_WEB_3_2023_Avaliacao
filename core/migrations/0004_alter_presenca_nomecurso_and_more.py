# Generated by Django 4.2.2 on 2023-06-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_presenca_nomealuno_alter_presenca_nomecurso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='NomeCurso',
            field=models.IntegerField(choices=[(1, 'DSM'), (2, 'GE'), (3, 'SI')], verbose_name='Nome_do_Curso'),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='NomeProfessor',
            field=models.IntegerField(choices=[(1, 'Orlando'), (2, 'Thiago'), (3, 'Angela'), (4, 'Nilton'), (5, 'Esdras'), (6, 'Leonardo')], verbose_name='Nome_do_Professor'),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='Semestre',
            field=models.IntegerField(choices=[(1, '1º Semestre'), (2, '2º Semestre'), (3, '3º Semestre'), (4, '4º Semestre'), (5, '5º Semestre'), (6, '6º Semestre')], verbose_name='Semestre'),
        ),
    ]