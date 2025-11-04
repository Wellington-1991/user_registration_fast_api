# User CRUD API com FastAPI

Este é um projeto de API para um CRUD (Create, Read, Update, Delete) de usuários, desenvolvido utilizando o framework Python **FastAPI**.

A aplicação segue uma arquitetura em camadas (Controllers, Services, Repositories) para uma melhor organização e manutenibilidade do código.

## 📖 Índice

- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Como Rodar o Projeto](#️-como-rodar-o-projeto)
- [Endpoints da API](#-endpoints-da-api)

## ✨ Funcionalidades

- 📝 Criar um novo usuário.
- 📄 Listar todos os usuários cadastrados.
- 👤 Obter um usuário específico pelo seu ID.
- 🔄 Atualizar os dados de um usuário (não implementado no controller, mas a base existe).
- 🗑️ Deletar um usuário (não implementado no controller, mas a base existe).

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma para separar as responsabilidades:

```
/app
├── api
│   └── controllers
│       └── users.py      # Define os endpoints da API (rotas).
├── db
│   ├── models
│   │   └── User.py       # Modelo da tabela de usuários (SQLAlchemy).
│   ├── base.py           # Base declarativa do SQLAlchemy e função de inicialização.
│   └── session.py        # Configuração do engine e sessão do banco de dados.
├── repositories
│   └── user_repository.py # Lógica de acesso direto ao banco de dados (CRUD).
├── schemas
│   └── user.py           # Schemas Pydantic para validação de dados de entrada e saída.
├── services
│   └── user_service.py   # Camada de serviço com a lógica de negócio.
└── main.py               # Ponto de entrada da aplicação FastAPI.
```

## 🚀 Tecnologias Utilizadas

As principais bibliotecas e frameworks utilizados neste projeto são:

- **Python 3.10+**
- **FastAPI**: Framework web para a construção da API.
- **SQLAlchemy**: ORM para interação com o banco de dados SQL.
- **Pydantic**: Para validação e serialização de dados.
- **Uvicorn**: Servidor ASGI para executar a aplicação.
- **Alembic** (Recomendado): Para gerenciar as migrações do banco de dados.

## ⚙️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
- [Python 3.10 ou superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- Um editor de código de sua preferência, como o [VSCode](https://code.visualstudio.com/).

## ▶️ Como Rodar o Projeto

Siga os passos abaixo para executar o projeto em seu ambiente local.

```bash
# 1. Clone o repositório (se ainda não o fez)
git clone <URL_DO_SEU_REPOSITORIO>
cd user_registration_fast_api

# 2. Crie e ative um ambiente virtual (recomendado)
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# 3. Instale as dependências
# Crie um arquivo 'requirements.txt' com as bibliotecas abaixo e execute:
pip install -r requirements.txt

# 4. Configure o banco de dados
# Verifique o arquivo app/db/session.py e ajuste a string de conexão
# com o banco de dados (DATABASE_URL) se necessário.

# 5. Execute a aplicação
uvicorn app.main:app --reload
```

Após executar o último comando, a aplicação estará disponível em `http://127.0.0.1:8000`.

Você pode acessar a documentação interativa gerada automaticamente pelo FastAPI em:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Endpoints da API

Os seguintes endpoints estão disponíveis:

- `GET /users/`: Retorna uma lista de todos os usuários.
- `POST /users/`: Cria um novo usuário.
  - **Body**: `{ "username": "string", "email": "user@example.com" }`
- `GET /users/{user_id}`: Retorna os detalhes de um usuário específico.

### Exemplo de `requirements.txt`

```
fastapi
uvicorn[standard]
sqlalchemy
pydantic
# Adicione aqui o driver do seu banco de dados, por exemplo:
# psycopg2-binary  # para PostgreSQL
# aiosqlite        # para SQLite assíncrono
```
