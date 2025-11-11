Desafio de Estágio: CRUD de Produtos (Django + AJAX)

Este projeto consiste na implementação de um sistema completo de gerenciamento de produtos (CRUD: Create, Read, Update, Delete), desenvolvido como parte de um desafio técnico. O sistema integra backend em Django com frontend dinâmico utilizando JavaScript (AJAX) para comunicação assíncrona, permitindo operações em tempo real sem recarregar a página.

Stack Utilizada
Camada	Tecnologia
Backend	Python 3.11+ + Django 5.2
Frontend	HTML5, CSS, JavaScript (Fetch API / AJAX)
Banco	SQLite (banco padrão do Django)
Funcionalidades Implementadas

CRUD completo de produtos

Siga as instruções abaixo para rodar o projeto localmente:

Pré-requisitos

Python 3.11+

Git

1. Clonar o repositório
REPO.git
git clone https://github.com/xXGu5tavoXx/crud-desafio-estagio.git

2. Criar e ativar o ambiente virtual

Windows:

python -m venv venv
venv\Scripts\activate

3. Instalar as dependências
pip install -r requirements.txt

4. Aplicar as migrações
python manage.py migrate

5. Executar o servidor
python manage.py runserver

6. Acessar no navegador
http://localhost:8000/
