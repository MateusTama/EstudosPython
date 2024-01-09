import mysql.connector

def mostrarMenu():
  print("Digite 1 para adicionar um novo usuário com login e senha na tabela; ")
  print("Digite 2 para verificar se um usuário com determinado login e senha existe na tabela;")
  print("Digite 3 para listar todos os usuários cadastrados na tabela.")

  opcao = int(input("Opção:"))
  return opcao

def usuarios(parlogin,parsenha):

  conexao = mysql.connector.connect(host="localhost",
                                    user="estudante",
                                    password="ifcbrusque")
  cursor = conexao.cursor()
  cursor.execute("CREATE DATABASE IF NOT EXISTS usuarios")
  conexao.database = "usuarios"
  cursor.execute(
    "CREATE TABLE IF NOT EXISTS usuarios (login varchar(50),senha char(8))")
  cursor.execute(
    f"INSERT INTO usuarios (login, senha) values ('{parlogin}', '{parsenha}')")
  conexao.commit()
  cursor.close()
  conexao.close()


def verificar_usuario(parverif_login, parverif_senha):
  conexao = mysql.connector.connect(host="localhost",
                                    user="estudante",
                                    password="ifcbrusque",
                                    database="usuarios")
  cursor = conexao.cursor()
  cursor.execute(
    f"SELECT * FROM usuarios WHERE login = '{parverif_login}' AND senha = '{parverif_senha}'"
  )
  resultado = cursor.fetchone()
  if resultado:
    print("O usuário foi encontrado na tabela!")
  else:
    print("O usuário não foi encontrado.")
  cursor.close()
  conexao.close()


def listar_usuarios():
  conexao = mysql.connector.connect(host="localhost",
                                    user="estudante",
                                    password="ifcbrusque",
                                    database="usuarios")
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM usuarios")
  usuarios = cursor.fetchall()

  print("Lista de usuários:")
  for usuario in usuarios:
    print(usuario)

  cursor.close()
  conexao.close()