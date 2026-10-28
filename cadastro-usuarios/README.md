# User Management System (Flask + MySQL)

A full CRUD web app (Create, Read, Update, Delete) for managing users, built with **Python**, **Flask** and **MySQL**.

**Keywords:** Python · Flask · MySQL · SQL · CRUD · REST-style routes · HTML · CSS · Jinja templates

## Features

- Create, list, edit and delete users
- Server-rendered pages with Flask and Jinja templates
- MySQL database with the schema in `database.sql`
- Database credentials read from environment variables (no secrets in the code)

## Tech stack

Python 3 · Flask · MySQL · mysql-connector-python · HTML · CSS

## How to run

```bash
git clone https://github.com/ArthurRodrigues0/sistema-cadastro-usuarios.git
cd sistema-cadastro-usuarios/cadastro-usuarios
pip install -r requirements.txt

# create the database
mysql -u root -p < database.sql

# set the connection (see .env.example)
export DB_HOST=localhost DB_USER=root DB_PASSWORD=your_password DB_NAME=cadastro_db DB_PORT=3307

python app.py
```

Then open http://127.0.0.1:5000.

---

## 🇧🇷 Em português

Sistema CRUD completo de cadastro de usuários feito com **Python (Flask)** e **MySQL**: cadastro, listagem, edição e exclusão.

Para rodar: instale as dependências com `pip install -r requirements.txt`, crie o banco com `database.sql`, defina as variáveis de ambiente do banco (veja `.env.example`) e execute `python app.py`.

## Author

**Arthur Rodrigues Chaves** · [LinkedIn](https://linkedin.com/in/arthur-rodrigues-267b9923a) · [GitHub](https://github.com/ArthurRodrigues0)
