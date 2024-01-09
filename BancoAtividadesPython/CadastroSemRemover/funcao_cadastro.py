import mysql.connector

def conectarBancoDados():

    try:
        conexao = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Rafaela5")
    except Exception as erro:
        print()
        print(f"Erro: {erro}")
    else:
        return conexao

def mostrarMenu():
    print()
    print("Selecione a opção desejada:")
    print()
    print("1 - Cadastrar novo usuário.")
    print("2 - Mostrar lista de usuários cadastrados.")
    print("3 - Checar se o usuário já está cadastrado.")
    print("4 - Excluir Banco de Dados.")
    print("0 - Sair")
    print()
    resposta = int(input("Número da sua opção: "))
    print()
    return resposta

def adicionarUsuario(parCursor):
    try:
        login = input("Insira seu login de até 8 dígitos: ")
        print()
        senha = input("Insira sua senha de até 4 dígitos: ")

        sql1 = f"SELECT * FROM usuario WHERE login = {login}"
        parCursor.execute(sql1)
        tabelaUsuario = parCursor.fetchall()
        print()
        if len(tabelaUsuario) == 0:
            sql = f"""INSERT INTO usuario
                                (login, senha) 
                            VALUES 
                                ({login}, {senha})
                """
            parCursor.execute(sql)
            print("Usuário Cadastrado com sucesso!")
        else:
            print("Esse usuário já estava cadastrado no sistema!")

    except Exception as erro:
        print()
        print(f"Erro: {erro}")

def verUsuarios(parCursor):
    try:
        sql = "SELECT * FROM usuario"
        parCursor.execute(sql)

        tabelaUsuarios = parCursor.fetchall()
        for linha in tabelaUsuarios:
            print(f"Usuário: {linha[0]} - Login: {linha[1]} Senha: {linha[2]}")

    except Exception as erro:
        print()
        print(f"Erro: {erro}")

def checarUsuario(parCursor):
    try:
        login = input("Informe o login do usuário: ")
        print()
        senha = input("Informe a senha do usuário: ")
        sql = f"SELECT * FROM usuario WHERE login = {login} AND senha = {senha}"
        parCursor.execute(sql)
        tabelaUsuario = parCursor.fetchall()
        print()
        if len(tabelaUsuario) == 0:
            print("Este usuário não está cadastrado.")
        else:
            print("Usuário cadastrado!")

    except Exception as erro:
        print()
        print(f"Erro: {erro}")
        
def excluirBanco(parCursor):
    try:
        banco = "cadastro"
        sql = f"DROP DATABASE {banco}"
        parCursor.execute(sql)
        print("Banco de Dados excluído.")
        
    except Exception as erro:
        print()
        print(f"Erro: {erro}")