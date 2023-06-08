from django.shortcuts import redirect, render
from .forms import PresencaForm
from .models import Presenca

def CadastroPresenca(request):
    if request.method == 'GET':
        form = PresencaForm()
        contexto = {
            'form': form
        }
        return render (request, "index.html", contexto)
    
    if request.method == 'POST':
        aluno = request.POST['NomeAluno']
        professor = request.POST['NomeProfessor']
        curso = request.POST['Curso']
        semestre = request.POST['Semestre']
        data = request.POST['DataPresenca']

        Presenca.objects.create(
            NomeAluno = aluno,
            NomeProfessor = professor,
            Semestre = semestre,
            NomeCurso = curso,
            DataPresenca = data,
        )
    return redirect('/')

def ListaPresenca(request):
    if request.method == "GET":
        dados = Presenca.objects.all()
        return render (request, 'list.html', {'dados':dados})
