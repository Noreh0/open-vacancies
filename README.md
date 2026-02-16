# OPEN VACANCIES (PT/EN)

## 🇧🇷 Português

### Visão geral
Sistema web para **abertura, avaliação e controle de vagas** internas.  
Os colaboradores solicitam vagas e o time de RH avalia, aprova ou rejeita.

### Funcionalidades
- Cadastro de vagas (solicitantes)
- Listagem de vagas
- Edição e exclusão (RH)
- Avaliação de vagas (RH)
- Aprovação / Rejeição
- Ativação / Desativação

### Perfis de acesso
- **Solicitante:** cria vagas.
- **RH:** controla todo o fluxo (listar, editar, avaliar, aprovar, rejeitar, ativar/desativar).

### Cenários de uso
- Abertura de vaga por reposição
- Abertura de nova vaga em um setor
- Validação de vaga pelo RH antes de iniciar recrutamento

### Como rodar localmente (Windows)
1. **Crie e ative o ambiente virtual**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. **Instale as dependências**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Aplique as migrações**
   ```powershell
   python manage.py migrate
   ```

4. **Crie o superusuário**
   ```powershell
   python manage.py createsuperuser
   ```

5. **Inicie o servidor**
   ```powershell
   python manage.py runserver
   ```

6. **Acesse**
   - `http://127.0.0.1:8000/` (criar vaga)
   - `http://127.0.0.1:8000/rh/` (painel RH)

---

## 🇺🇸 English

### Overview
Web system for **opening, evaluating and managing internal vacancies**.  
Employees submit vacancy requests and HR evaluates, approves or rejects.

### Features
- Vacancy creation (requesters)
- Vacancy listing
- Edit and delete (HR)
- Vacancy evaluation (HR)
- Approve / Reject
- Activate / Deactivate

### Access roles
- **Requester:** can create vacancies.
- **HR:** full control (list, edit, evaluate, approve, reject, activate/deactivate).

### Use cases
- Replacement hiring
- New position request
- HR validation before recruitment starts

### How to run locally (Windows)
1. **Create and activate virtual environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```powershell
   python manage.py migrate
   ```

4. **Create superuser**
   ```powershell
   python manage.py createsuperuser
   ```

5. **Run server**
   ```powershell
   python manage.py runserver
   ```

6. **Access**
   - `http://127.0.0.1:8000/` (create vacancy)
   - `http://127.0.0.1:8000/rh/` (HR panel)
---
## License
MIT (or update as needed)
