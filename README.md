# FATEC_DES_WEB_3_2023_Avaliacao
Projeto criado no framework Django, para gestão de presença de alunos.

## Ideia Principal
Na semana da carreira deste ano, ocorreu um fato histórico: pela primeira vez, realizamos este evento fora da sede da Fatec Araras. No teatro estadual, assistimos a uma palestra e após o evento, os alunos precisaram encontrar docentes para escanear um QR-Code, que direcionava a um formulário de envio de dados.

Para o ano que vem, a equipe no NAC ( https://fatecararas.cps.sp.gov.br/nac-nucleo-de-apoio-a-carreira/) conta com o seu apoio. Desenvolva um sistema em Django com testes unitários para cadastrar a presença e apresentar os alunos que se cadastraram no dia do evento.

## No sistema é possível:
1 - Fornecer seu nome completo; <br>
2 - Selecionar as informações de "Nome do Professor", "Nome do Curso" e "Semestre", a partir de opções prestabelecidas; <br>
3 - Registar tais informações no banco de dados; <br>
4 - Listar todos os alunos que registraram presença. <br>

# Configurações do projeto:
Para instalar as dependências do projeto, basta apenas criar o ambiente virtual, com o `python3 -m venv venv `, e executar o comando `pip install -r requirements.txt`<br>
Após isso, é necessário realizar o migrate `py manage.py migrate`, que criará o banco para o andamento do projeto. <br>
E para startar o projeto `py manage.py runserver`
