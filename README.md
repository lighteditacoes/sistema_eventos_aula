# ATIVIDADE PRÁTICA — SISTEMA DE GERENCIAMENTO DE EVENTOS

## Objetivo

Transformar o front-end fornecido em uma aplicação web funcional 
utilizando Python, Flask, Jinja2, SQLite e Flask-SQLAlchemy.

O sistema deverá permitir o cadastro e o gerenciamento de eventos.

## Funcionalidades

A aplicação deverá permitir:

* Visualizar a página inicial;
* Listar os eventos cadastrados;
* Cadastrar um novo evento;
* Visualizar os detalhes de um evento;
* Editar um evento;
* Excluir um evento.

## Dados do evento

Cada evento deverá possuir:

* ID;
* Nome;
* Descrição;
* Data;
* Local;
* Categoria;
* Quantidade de participantes.

## Requisitos

O projeto deverá:

1. Utilizar Flask para criação da aplicação;
2. Organizar as páginas na pasta `templates/`;
3. Criar um template base (`base.html`) contendo a estrutura comum das páginas;
4. Utilizar herança de templates do Jinja2, fazendo com que as demais páginas aproveitem o `base.html`;
5. Organizar CSS e JavaScript na pasta `static/`;
6. Utilizar rotas Flask para as funcionalidades do sistema;
7. Utilizar `url_for()` para os links da aplicação;
8. Utilizar Jinja2 para apresentar os dados dinamicamente;
9. Utilizar formulários HTML para cadastro e edição;
10. Utilizar `request` para receber os dados enviados pelos formulários;
11. Utilizar SQLite como banco de dados;
12. Utilizar Flask-SQLAlchemy para trabalhar com o banco;
13. Criar um model `Evento`;
14. Implementar as operações de CRUD.

## Rotas esperadas

A aplicação deverá possuir, no mínimo:

```text
/                    → Página inicial
/eventos             → Lista de eventos
/cadastrar           → Cadastro de evento
/evento/<id>         → Detalhes do evento
/editar/<id>         → Edição do evento
/excluir/            → Exclusão do evento
```

## Observação

O front-end fornecido deve ser utilizado como ponto de partida.   
O foco da atividade é transformar as páginas estáticas em uma aplicação dinâmica, 
integrando Flask, Jinja2 e banco de dados.
