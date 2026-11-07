# Documentação do Projeto

## TechFlow Solutions

Sistema de gerenciamento de tarefas desenvolvido em Python.

## Objetivo

Organizar tarefas, prioridades e acompanhar o andamento das atividades.

## Metodologia

Kanban, utilizando as colunas:

- Todo
- In Progress
- Done

## Funcionalidades do Sistema

- Cadastro de tarefas.
- Consulta de tarefas.
- Edição de tarefas.
- Exclusão de tarefas.
- Definição de prioridades.
- Acompanhamento do status das tarefas.
- Filtro de tarefas por status.

## Mudança de Escopo

Durante o desenvolvimento do sistema TechFlow Solutions, foi identificada a necessidade de adicionar uma nova funcionalidade ao projeto.

**Nova funcionalidade:** Filtro de tarefas por status.

**Descrição:** Permitir que o usuário visualize somente as tarefas de acordo com o status selecionado:

- A Fazer
- Em Progresso
- Concluída

**Justificativa:** A funcionalidade facilita a organização e o acompanhamento das tarefas, permitindo que o usuário encontre rapidamente as atividades de cada etapa.

**Impacto no projeto:** Foi necessário atualizar o menu principal, implementar a função de filtragem e adicionar testes automatizados para verificar seu funcionamento.

**Metodologia:** A mudança foi registrada no quadro Kanban e acompanhada durante o desenvolvimento.

## Tecnologias Utilizadas

- Python
- Git e GitHub
- GitHub Projects
- GitHub Actions
- Testes automatizados com unittest

## Testes

O projeto possui testes automatizados para verificar o funcionamento das principais funcionalidades do sistema, incluindo o filtro de tarefas por status.

Os testes são executados automaticamente por meio do GitHub Actions.
