<div align="center">

# 🎬 CineFlow — Movie Library

Uma aplicação web para gerenciamento e catalogação de filmes (CRUD completo), inspirada na estética visual do **Letterboxd**.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

</div>

---

## 📌 Sobre o Projeto

Desenvolvido para a disciplina **Computational Thinking with Python**, o projeto implementa um fluxo completo de gerenciamento de biblioteca de filmes:

- **Create:** Cadastro de novos filmes com título e gênero (`/add`).
- **Read:** Exibição do catálogo em pôsteres verticais no formato clássico 2:3 (`/movies`).
- **Update:** Edição de dados de filmes existentes com campos pré-carregados (`/edit/{id}`).
- **Delete:** Exclusão em lote por caixas de seleção nativas (`/delete-movies`).

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/raulacor/CP-04-Computational-Thinking-With-Python.git
   cd CP-04-Computational-Thinking-With-Python
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv .venv
   # No Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # No Linux/macOS:
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart
   ```

4. **Inicie o servidor:**
   ```bash
   cd src
   uvicorn main:app --reload
   ```

5. Acesse no seu navegador:
   👉 **http://127.0.0.1:8000/movies**

---

## 📂 Estrutura de Pastas

```text
├── pages/                # Templates e estilos do Front-end
│   ├── add/              # Tela de cadastro (add.html e add.css)
│   ├── edit/             # Tela de edição (edit.html e edit.css)
│   └── list/             # Catálogo de filmes (list.html e list.css)
│
└── src/                  # Código-fonte da aplicação (Back-end)
    ├── controller/       # Rotas e controladores FastAPI (api.py)
    ├── database/         # Conexão e queries SQLite (db.py)
    └── main.py           # Ponto de entrada da aplicação
```

---

## 👥 Integrantes

* **João Pedro** — [@Jottape11](https://github.com/Jottape11)
* **Raul Corsi** — [@raulacor](https://github.com/raulacor)
