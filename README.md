# StockControl

Sistema desenvolvido em **Python** para gerenciamento de estoque de folhas impressas utilizadas por pizzarias.

O projeto foi criado com o objetivo de praticar conceitos de programação, organização de código, persistência de dados e desenvolvimento de sistemas de controle de estoque.

## Funcionalidades

* ✅ Cadastro de pizzarias
* ✅ Consulta de estoque por nome
* ✅ Adição de folhas ao estoque
* ✅ Remoção de folhas do estoque
* ✅ Exclusão de cadastros
* ✅ Listagem de todas as pizzarias
* ✅ Alerta automático para estoques baixos
* ✅ Persistência de dados em arquivos JSON
* ✅ Histórico de movimentações (entradas e saídas)
* ✅ Relatórios de estoque
* ✅ Interface gráfica utilizando CustomTkinter

## Relatórios disponíveis

* Total de folhas em estoque
* Total de cadastros
* Estoques com quantidade baixa
* Histórico completo de movimentações

## Tecnologias utilizadas

* Python
* CustomTkinter
* JSON
* Módulo `datetime`
* Git/GitHub

## Estrutura do projeto

```text
StockControl/
│
├── stockcontrol.py      # Regras do sistema e funções de estoque
├── interface.py         # Interface gráfica
├── estoque.json         # Dados do estoque
├── historico.json       # Histórico de movimentações
└── README.md