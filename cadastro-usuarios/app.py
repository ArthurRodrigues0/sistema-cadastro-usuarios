from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# conexão com o banco
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arthur2309+",
        database="cadastro_db",
        port=3307
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/add', methods=['POST'])
def add_user():
    nome = request.form['nome']
    email = request.form['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        cursor.execute(
            "UPDATE usuarios SET nome=%s, email=%s WHERE id=%s",
            (nome, email, id)
        )
        conn.commit()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    conn.close()

    return render_template('edit.html', usuario=usuario)


if __name__ == '__main__':
    app.run(debug=True)


