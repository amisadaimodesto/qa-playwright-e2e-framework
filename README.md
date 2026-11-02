# QA Automation Framework - Playwright & Python E2E

Estrutura de automação de testes End-to-End (E2E) construída com Python, Playwright e Pytest, aplicando o padrão **Page Object Model (POM)**, massa de dados desacoplada e containerização completa com Docker.

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.12+
- **Test Runner:** Pytest 9.x
- **Automação Web:** Playwright
- **Relatórios:** Allure Framework
- **Containerização:** Docker & Docker Compose
- **Design Pattern:** Page Object Model (POM)

## 📁 Estrutura do Projeto

```text
qa-playwright-e2e-framework/
├── configs/             # Configurações globais e de ambiente
├── reports/             # Artefatos de execução (Allure e screenshots)
├── tests/
│   ├── data/            # Massas de teste desacopladas (JSON)
│   ├── pages/           # Classes Page Object Model
│   ├── conftest.py      # Fixtures compartilhadas e captura de prints
│   ├── test_cart.py     # Suíte de carrinho e fluxo de compra
│   └── test_login.py    # Suíte de autenticação
├── docker-compose.yml   # Orquestração do container de testes
├── Dockerfile           # Imagem base de execução headless
├── pytest.ini           # Configuração de execução do Pytest
└── requirements.txt     # Dependências congeladas
```

## 🚀 Como Executar

### 1. Execução Local (com venv)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install --with-deps

# Executar suíte em modo headless
pytest

# Executar com navegador visível
pytest --headed
```

### 2. Execução Containerizada (Docker)

```bash
# Build e execução via Docker Compose
docker compose build
docker compose run --rm e2e-tests
```