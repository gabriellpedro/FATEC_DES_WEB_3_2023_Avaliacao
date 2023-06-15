from django.test import TestCase
from core.forms import PresencaForm
from core.models import Presenca

class IndexTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_text(self):
        self.assertContains(self.response, 'Registro Presença')
    
    def test_template_index(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_template_noIndex(self):
        self.assertTemplateNotUsed(self.response, "list.html")

class ListaTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/lista')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_text(self):
        self.assertContains(self.response, 'Listagem de presença')
    
    def test_template_index(self):
        self.assertTemplateUsed(self.response, "list.html")

    def test_template_noIndex(self):
        self.assertTemplateNotUsed(self.response, "index.html")

class BancoTest(TestCase):
    def setUp(self):
        presenca_1 = {
            'NomeAluno' : 'Gabriel Pedro',
            'NomeProfessor' : 1,
            'Semestre' : 3,
            'NomeCurso' : 1
        }

        presenca_2 = {
            'NomeAluno' : 'Gabriel Pedro',
            'NomeProfessor' : None,
            'Semestre' : 3,
            'NomeCurso' : 1
        }

        self.aluno_presenca = PresencaForm(presenca_1)
        self.aluno_presenca_fail = PresencaForm(    presenca_2)
        self.aluno_presenca.is_valid()
        self.aluno_presenca_banco = Presenca(**self.aluno_presenca.cleaned_data)

    def test_tipo(self):
        self.assertIs(type(self.aluno_presenca), PresencaForm)
        self.assertIs(type(self.aluno_presenca_banco), Presenca)

    def test_presenca_form(self):
        self.assertTrue(self.aluno_presenca.is_valid())

    def test_presenca_form_fields(self):
        self.aluno_presenca.is_valid()
        self.assertEqual(self.aluno_presenca.cleaned_data.get('NomeAluno'), 'Gabriel Pedro')
        self.assertEqual(self.aluno_presenca.cleaned_data.get('NomeProfessor'), 1)
        self.assertEqual(self.aluno_presenca.cleaned_data.get('Semestre'), 3)
        self.assertEqual(self.aluno_presenca.cleaned_data.get('NomeCurso'), 1)

    def test_campo_null(self):
        self.assertFalse(self.aluno_presenca_fail.is_valid())
    
