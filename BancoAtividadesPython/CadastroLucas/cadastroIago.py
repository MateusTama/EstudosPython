import mysql.connector

password = input("Insira sua senha: ")
# Dados de conexão com o banco de dados
host = "localhost"
user = "root"
password = password
database = "iago"

# Função para criar tabela "usuarios"
def criar_tabela_usuarios(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            login VARCHAR(20) NOT NULL,
            senha VARCHAR(20) NOT NULL
        )
    """)

# Função para adicionar um novo usuário
def adicionar_usuario(cursor, login, senha):
    cursor.execute("INSERT INTO usuarios (login, senha) VALUES (%s, %s)", (login, senha))
    print("Usuário adicionado com sucesso")

# Função para verificar se um usuário com determinado login e senha existe
def verificar_usuario(cursor, login, senha):
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE login = %s AND senha = %s", (login, senha))
    result = cursor.fetchone()[0]
    if result == 1:
        print("Usuário autenticado com sucesso")
    else:
        print("Usuário não encontrado")

# Função para listar todos os usuários cadastrados
def listar_usuarios(cursor):
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        print("ID: {}, Login: {}, Senha: {}".format(*row))

# Função principal que apresenta o menu
def main():
    # Conexão com o banco de dados
    try:
        conexao = mysql.connector.connect(host=host, user=user, password=password, database=database)
    except mysql.connector.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return

    cursor = conexao.cursor()

    criar_tabela_usuarios(cursor)

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar novo usuário")
        print("2. Verificar usuário existente")
        print("3. Listar usuários cadastrados")
        print("0. Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            login = input("Digite o login do novo usuário: ")
            senha = input("Digite a senha do novo usuário: ")
            adicionar_usuario(cursor, login, senha)
            conexao.commit()
        elif opcao == "2":
            login = input("Digite o login do usuário: ")
            senha = input("Digite a senha do usuário: ")
            verificar_usuario(cursor, login, senha)
        elif opcao == "3":
            listar_usuarios(cursor)
        elif opcao == "0":
            break
        else:
            print("Opção inválida")

    cursor.close()
    conexao.close()

main()
