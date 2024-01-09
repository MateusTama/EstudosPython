from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os
import time

# Inicialização da aplicação Flask
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'
app.config['UPLOAD_FOLDER'] = 'Trabalho Final/static/images/uploads'

password = input("Insira sua senha: ")

# Configuração do banco de dados
conexao = mysql.connector.connect(  user ='root',
                                    password = password,
                                    host = 'localhost',
                                    database = 'trabalho_final')

cursor = conexao.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("""
        SELECT postagens.*, usuarios.nome as usuario_nome 
        FROM postagens, usuarios 
        WHERE postagens.usuario_id = usuarios.id 
        ORDER BY postagens.data_postagem DESC
    """)
    postagens = cursor.fetchall()
    conteudo = render_template('index.html', postagens=postagens)
    return conteudo

@app.route('/user/<user_id>')
def user_posts(user_id):
    cursor.execute(f"""
        SELECT postagens.*, usuarios.nome as usuario_nome 
        FROM postagens, usuarios 
        WHERE postagens.usuario_id = usuarios.id 
        AND usuarios.id = {user_id}
        ORDER BY postagens.data_postagem DESC
    """)
    
    postagens = cursor.fetchall()
    
    nome = postagens[0]["usuario_nome"]

    conteudo = render_template('user_posts.html', postagens=postagens, usuario_nome=nome)
    return conteudo 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)

        cursor.execute(f"INSERT INTO usuarios (nome, email, senha_hash) VALUES ('{nome}', '{email}', '{senha_hash}')" )
        conexao.commit()
        conteudo = redirect('/')
        return conteudo
    else:
        conteudo = render_template('register.html')
        return conteudo

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cursor.execute(f"SELECT * FROM usuarios WHERE email = '{email}'")
        usuario = cursor.fetchone()
        if usuario:
            senha_correta = check_password_hash(usuario['senha_hash'], senha)
        
        if usuario and senha_correta:
            session['usuario_id'] = usuario['id']
            session['usuario_nome'] = usuario['nome']  # Armazenando o nome do usuário na sessão
            conteudo = redirect("/")
            return conteudo
    else:
        conteudo = render_template('login.html')
        return conteudo

@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    conteudo = redirect("/")
    return conteudo

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'usuario_id' not in session:
        conteudo = render_template('login.html')
        return conteudo

    if request.method == 'POST':
        agora = time.time()
        foto = request.files['foto']
        nome_arquivo_foto =  f"{agora}{foto.filename}"
        descricao = request.form['descricao']

        if foto:
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo_foto)
            foto.save(foto_path)

            cursor.execute(f"INSERT INTO postagens (usuario_id, foto, descricao) VALUES ('{session['usuario_id']}','{nome_arquivo_foto}','{descricao}')")
            conexao.commit()

            conteudo = redirect("/")
            return conteudo
    else:
        conteudo = render_template('upload.html')
        return conteudo 

if __name__ == '__main__':
    app.run(debug=True)
