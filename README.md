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

# Executar com intervalo visual entre passos (500ms)
pytest --headed --slowmo 500

# Executar teste específico interrompendo no primeiro erro
PWDEBUG=1 pytest -k "test_successful_login" -x
```

### 2. Modo Interativo & Relatórios Allure

```bash
# Executar gravando traces e dados para o Allure
pytest --tracing=on --alluredir=reports/allure-results

# Executar em modo debug interativo e gerar relatório
PWDEBUG=1 pytest -s --tracing=on --alluredir=reports/allure-results

# Gerar o relatório estático HTML
allure generate reports/allure-results -o reports/allure-report --clean

# Abrir o dashboard Allure no navegador (compatível com WSL)
allure open reports/allure-report -h 0.0.0.0 -p 8080
```

### 3. Execução Containerizada (Docker)

```bash
# Build e execução via Docker Compose
docker compose build
docker compose run --rm e2e-tests
```