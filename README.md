Desafio de Estágio: CRUD de Produtos (Django + AJAX)
Este projeto consiste na implementação de um sistema completo de gerenciamento de produtos (CRUD: Create, Read, Update, Delete), desenvolvido como parte de um desafio técnico. O sistema integra backend em Django com frontend dinâmico utilizando JavaScript (AJAX) para comunicação assíncrona, permitindo operações em tempo real sem recarregar a página.
Stack Utilizada
Camada
Tecnologia
Detalhes
Backend
Python 3.11+ + Django 5.2
Implementação da API RESTful, Modelagem de Dados (ORM) e Lógica de Negócio.
Frontend
HTML5, CSS, JavaScript (Fetch API / AJAX)
Interface de usuário dinâmica, responsável por todas as interações assíncronas com a API.
Banco de Dados
SQLite
Banco de dados padrão do Django para desenvolvimento.
Funcionalidades Implementadas
CRUD Completo: Criação, Leitura, Edição e Exclusão de produtos.
Validação de Dados: Validação no Backend (Django) para garantir que nome não seja vazio e que preco e quantidade sejam positivos.
Busca Parcial: Funcionalidade de pesquisa por nome de produto (case-insensitive) utilizando o lookup icontains.
Interface Dinâmica: Todas as operações são realizadas via AJAX, atualizando a tabela de produtos sem recarregar a página.
Desafios Técnicos Superados
O desenvolvimento exigiu a superação de desafios comuns em projetos Full-Stack, demonstrando a capacidade de depuração e resolução de problemas:
Desafio Técnico
Causa do Problema
Solução Implementada
Erro de Migração de Banco de Dados
Tentativa de aplicar migrações sem ter o modelo Produto totalmente definido ou após alterações no DecimalField sem default ou null.
Resolução: Exclusão de arquivos de migração antigos e do db.sqlite3 (ambiente de desenvolvimento) e aplicação correta do python manage.py makemigrations seguido de python manage.py migrate.
Bloqueio de Requisições POST/PUT/DELETE (CSRF)
O Django bloqueia requisições que modificam dados vindas de fontes externas ou sem o token de segurança.
Resolução: Implementação da lógica JavaScript para extrair o token CSRF do cookie ou do template e incluí-lo no cabeçalho (X-CSRFToken) de todas as requisições AJAX que modificam dados.
Instruções para Rodar o Projeto Localmente
Siga as instruções abaixo para rodar o projeto localmente:
Pré-requisitos
Python 3.11+
Git
1. Clonar o Repositório
Bash
git clone https://github.com/xXGu5tavoXx/crud-desafio-estagio.git
cd crud_challenge
2. Criar e Ativar o Ambiente Virtual
Bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows PowerShell )
venv\Scripts\activate
3. Instalar as Dependências
Com o ambiente virtual ativado:
Bash
pip install -r requirements.txt
4. Aplicar as Migrações
Bash
python manage.py migrate
5. Executar o Servidor
Bash
python manage.py runserver
6. Acessar no Navegador
O projeto estará acessível em:
Plain Text
http://localhost:8000/
