from django.shortcuts import redirect, render

from core.enums import CURSOS, PROFESSORES, SEMESTRES
from .forms import PresencaForm
from .models import Presenca

def index(request):
    form = PresencaForm(request.POST)
    contexto = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            form_save = Presenca(**form.cleaned_data)
            form_save.save()
            return redirect('/')
        else:
            return render(request, "index.html")
    else:             
        return render (request, "index.html", contexto)

def ListaPresenca(request):
    if request.method == "GET":
        dados = Presenca.objects.all()
        lista_presenca = list()
        for item in  dados:
            presenca = {
                'nome_aluno' : item.NomeAluno,
                'nome_professor' : PROFESSORES [item.NomeProfessor -1][1],
                'semestre' : SEMESTRES [item.Semestre -1][1],
                'curso': CURSOS [item.NomeCurso -1][1]
            }
            lista_presenca.append(presenca)
        dados = lista_presenca
        return render (request, 'list.html', {'dados': dados})
