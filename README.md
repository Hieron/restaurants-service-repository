# Nome do Projeto

Projeto relativo ao curso MBA em Engenharia de Software da Universidade Federal do Rio de Janeiro implementado pelo Grupo D para a segunda tarefa da disciplina Arquitetura de Serviços.

## Índice

1. [Visão Geral](#visão-geral)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Como Usar](#como-usar)
6. [Como Testar](#como-testar)

## Visão Geral

Este repositório contém o código-fonte de um serviço para cadastro e gerenciamento de restaurantes. O sistema oferece funcionalidades para criação, leitura, atualização e exclusão (CRUD) de restaurantes, além de permitir consultas baseadas em diferentes atributos do endereço.

## Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias e ferramentas:

- Flask: Framework web em Python para construção do serviço RESTful.
- Flask-SQLAlchemy: Extensão do Flask para integração com banco de dados SQL.
- SQLite: Banco de dados utilizado para armazenamento dos dados dos restaurantes.

## Instalação

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/hieron/restaurants-service-repository.git
cd restaurants-service-repository
```

### Passo 2: Criar o ambiente virtual

```bash
python -m venv venv
```

### Passo 3: Ativar o ambiente virtual

```bash
No Windows:
venv\Scripts\activate

No Mac/Linux:
source venv/bin/activate
```

### Passo 4: Instalação das dependências

```bash
pip install -r requirements.txt
```

### Passo 5: Desativar o ambiente virtual

```bash
deactivate
```

## Como Usar

Para inicializar o serviço utilize o seguinte comando:
```bash
python run.py
```

## Como Testar

Para inicializar o script de teste utilize o seguinte comando em outro terminal:
```bash
cd client
python script.py
```