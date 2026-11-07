# TechFlow Solutions — Sistema de Gerenciamento de Tarefas

## 1. Descrição do Projeto

O projeto consiste no desenvolvimento de um sistema de gerenciamento de tarefas para a empresa fictícia TechFlow Solutions, especializada em soluções de software.

A empresa foi contratada por uma startup do setor de logística que necessita de uma ferramenta para organizar suas atividades, acompanhar o andamento dos trabalhos e melhorar a produtividade da equipe.

O sistema será desenvolvido utilizando a linguagem Python e terá como objetivo facilitar o gerenciamento das tarefas, permitindo que os responsáveis acompanhem as atividades de maneira organizada.

## 2. Objetivo do Projeto

Desenvolver um sistema simples e funcional que permita:

- Cadastrar novas tarefas.
- Consultar tarefas cadastradas.
- Editar informações das tarefas.
- Excluir tarefas.
- Definir prioridades para as atividades.
- Acompanhar o andamento das tarefas.
- Identificar atividades pendentes e concluídas.

Com essas funcionalidades, pretende-se melhorar a organização e o acompanhamento das atividades da equipe.

## 3. Escopo do Projeto

O sistema contará inicialmente com as seguintes funcionalidades:

- **Cadastro:** permitir a criação de novas tarefas.
- **Consulta:** visualizar as tarefas cadastradas.
- **Edição:** modificar informações de tarefas existentes.
- **Exclusão:** remover tarefas cadastradas.
- **Priorização:** classificar tarefas conforme seu nível de prioridade.
- **Acompanhamento:** identificar se uma tarefa está pendente, em andamento ou concluída.

O desenvolvimento inicial será concentrado nas funcionalidades essenciais de gerenciamento de tarefas. Novas funcionalidades poderão ser adicionadas conforme as necessidades identificadas durante o projeto.

## 4. Metodologia Ágil Adotada

A metodologia escolhida para o desenvolvimento será o **Kanban**.

O Kanban é uma metodologia de organização visual do trabalho que permite acompanhar o andamento das atividades por meio de um quadro dividido em etapas.

Para este projeto, será utilizado o GitHub Projects, com três colunas principais:

- **A Fazer (To Do):** tarefas que ainda precisam ser realizadas.
- **Em Progresso (In Progress):** tarefas que estão sendo desenvolvidas.
- **Concluído (Done):** tarefas que já foram finalizadas.

Essa metodologia permitirá organizar as atividades, acompanhar o progresso do desenvolvimento e identificar possíveis atrasos ou dificuldades.

## 5. Tecnologias Utilizadas

- **Python:** linguagem utilizada para desenvolver o sistema.
- **GitHub:** plataforma para armazenar e controlar as versões do projeto.
- **GitHub Projects:** ferramenta para organização das tarefas utilizando Kanban.
- **GitHub Actions:** ferramenta para automatizar a execução dos testes e o controle de qualidade.

## 6. Estrutura Inicial do Projeto

A organização inicial dos arquivos será:

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
│
├── .github/
│   └── workflows/
│
└── README.md
```

## 7. Instruções para Executar o Sistema

Para executar o projeto, será necessário:

1. Ter o Python instalado no computador.
2. Clonar ou baixar o repositório do GitHub.
3. Abrir a pasta do projeto em um terminal.
4. Executar o comando:

```bash
python src/main.py
```

## 8. Controle de Qualidade

O projeto utilizará testes automatizados para verificar o funcionamento das funcionalidades desenvolvidas.

Também será configurado um pipeline utilizando GitHub Actions para executar os testes automaticamente e auxiliar na identificação de erros durante o desenvolvimento.

## 9. Gestão de Mudanças

Durante o desenvolvimento, poderá ocorrer uma alteração no escopo inicial do projeto.

Caso seja identificada a necessidade de adicionar uma nova funcionalidade, ela será documentada e incluída no quadro Kanban, permitindo acompanhar sua implementação e seus impactos no planejamento.

As alterações realizadas serão registradas no README e no histórico de commits do GitHub, mantendo a documentação atualizada.

---

**Projeto:** TechFlow Solutions — Sistema de Gerenciamento de Tarefas  
**Linguagem:** Python  
**Metodologia Ágil:** Kanban  
**Plataforma de versionamento:** GitHub
