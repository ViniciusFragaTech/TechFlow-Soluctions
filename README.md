# TechFlow Solutions — Sistema de Gerenciamento de Tarefas

## 1. Descrição do Projeto

O projeto consiste no desenvolvimento de um sistema de gerenciamento de tarefas para a empresa fictícia TechFlow Solutions, especializada em soluções de software.

A empresa foi contratada por uma startup do setor de logística que necessita de uma ferramenta para organizar suas atividades, acompanhar o andamento dos trabalhos e melhorar a produtividade da equipe.

O sistema será desenvolvido utilizando a linguagem Python e permitirá que os responsáveis acompanhem as atividades de maneira organizada.

## 2. Objetivo do Projeto

Desenvolver um sistema simples e funcional que permita:

- Cadastrar novas tarefas.
- Consultar tarefas cadastradas.
- Editar informações das tarefas.
- Excluir tarefas.
- Definir prioridades para as atividades.
- Acompanhar o andamento das tarefas.
- Filtrar tarefas conforme seu status.

## 3. Escopo do Projeto

O sistema possui as seguintes funcionalidades:

- **Cadastro:** permite criar novas tarefas.
- **Consulta:** permite visualizar as tarefas cadastradas.
- **Edição:** permite modificar informações das tarefas existentes.
- **Exclusão:** permite remover tarefas cadastradas.
- **Priorização:** permite classificar tarefas como Baixa, Média ou Alta.
- **Acompanhamento:** permite identificar o status de cada tarefa.
- **Filtro por status:** permite visualizar somente as tarefas de acordo com o status selecionado.

## 4. Metodologia Ágil Adotada

A metodologia escolhida para o desenvolvimento foi o **Kanban**.

O Kanban permite acompanhar o andamento das atividades por meio de um quadro dividido em três etapas:

- **Todo (A Fazer):** tarefas que ainda precisam ser realizadas.
- **In Progress (Em Progresso):** tarefas que estão sendo desenvolvidas.
- **Done (Concluído):** tarefas que já foram finalizadas.

Para organizar as atividades, foi utilizado o GitHub Projects.

## 5. Tecnologias Utilizadas

- **Python:** linguagem utilizada para desenvolver o sistema.
- **GitHub:** plataforma para armazenar e controlar as versões do projeto.
- **GitHub Projects:** ferramenta para organização das tarefas utilizando Kanban.
- **GitHub Actions:** ferramenta para automatizar a execução dos testes.
- **unittest:** biblioteca utilizada para criar os testes automatizados.
- **JSON:** formato utilizado para armazenar as tarefas.

## 6. Estrutura do Projeto

A organização dos arquivos está dividida da seguinte maneira:

```text
TechFlow-Solutions/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── docs/
│   ├── documentacao.md
│   ├── diagrama_casos_de_uso.md
│   ├── diagrama_de_classes.md
│   └── fluxograma.md
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── README.md
└── tarefas.json (criado durante a execução)
```

## 7. Instruções para Executar o Sistema

Para executar o projeto, será necessário:

1. Ter o Python instalado no computador.
2. Clonar ou baixar o repositório do GitHub.
3. Abrir a pasta do projeto em um terminal.
4. Executar o seguinte comando:

```bash
python src/main.py
```

O sistema apresentará um menu com as opções disponíveis para gerenciamento das tarefas.

## 8. Controle de Qualidade

O projeto utiliza testes automatizados com a biblioteca unittest para verificar o funcionamento das funcionalidades implementadas.

Também foi configurado um fluxo de integração contínua utilizando GitHub Actions, responsável por executar os testes automaticamente após alterações no repositório.

## 9. Gestão de Mudanças

Durante o desenvolvimento, foi identificada a necessidade de adicionar uma nova funcionalidade ao escopo inicial.

**Nova funcionalidade: Filtro de tarefas por status.**

A funcionalidade permite visualizar tarefas conforme os seguintes status:

- A Fazer.
- Em Progresso.
- Concluída.

A alteração foi implementada no sistema, registrada na documentação e acompanhada pelo quadro Kanban.

Também foram atualizados os testes automatizados para verificar o funcionamento do filtro.

## 10. Persistência dos Dados

As tarefas são armazenadas em um arquivo JSON, permitindo que as informações cadastradas sejam recuperadas quando o sistema for iniciado novamente.

## 11. Informações do Projeto

- **Projeto:** TechFlow Solutions — Sistema de Gerenciamento de Tarefas.
- **Linguagem:** Python.
- **Metodologia Ágil:** Kanban.
- **Plataforma de versionamento:** GitHub.
- **Testes automatizados:** unittest.
- **Integração contínua:** GitHub Actions.
