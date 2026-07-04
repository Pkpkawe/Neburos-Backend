# Neburos Backend
API responsável pela lógica de funcionamento do **Neburos**, um sistema de gerenciamento financeiro **open source e gratuito**.

---

## Tecnologias / Ferramentas
- **Python**  
- **FastAPI**  
- **Pytest**  
- **uv** (gerenciador de dependências)  
- **Git** e **GitHub**  

---

## Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/Pkpkawe/Neburos-Backend.git ./api
cd api
```

### 2. Configure o ambiente
Crie o arquivo `.env` a partir do exemplo:
```bash
cp .env-example .env
```
Edite os valores conforme sua necessidade (ex: banco de dados, chaves de API).

### 3. Instale as dependências
```bash
uv sync
```

### 4. Execute o servidor
```bash
uv run src/main.py
```

---

## Testes
Para rodar os testes automatizados:
```bash
uv run pytest
```

---

## Estrutura do Projeto
```
└── 📁api
    └── 📁.github
        └── 📁ISSUE_TEMPLATE
            ├── 01 - default.md
            ├── 02 - bug_report.md
            ├── 03 - feature_request.md
        ├── pull_request_template.md
    └── 📁src
        └── 📁__pycache__
        └── 📁configs
            ├── __init__.py
            ├── loggin_config.py
            ├── settings.py
        └── 📁core
            ├── __init__.py
        └── 📁depends
            ├── __init__.py
        └── 📁models
            ├── __init__.py
        └── 📁routes
            ├── __init__.py
        └── 📁schemas
            ├── __init__.py
        └── 📁tests
            ├── __init__.py
            ├── test_init.py
        ├── main.py
    ├── .editorconfig
    ├── .env-example
    ├── .gitignore
    ├── .python-version
    ├── LICENSE
    ├── pyproject.toml
    ├── pytest.ini
    ├── README.md
    └── uv.lock
```
