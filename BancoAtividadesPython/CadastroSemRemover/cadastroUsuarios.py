#Importar banco de dados mysql
import mysql.connector
import funcao_cadastro

#Conectar Banco de dados
conexao = funcao_cadastro.conectarBancoDados()
print("Banco de Dados MYSQL conectado.")

#conectar cursor ao mysql
cursor = conexao.cursor()

#criar banco de dados
print()
cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro")
print("Banco de dados criado com sucesso.")

#conectar ao banco de dados
conexao.database = "cadastro"

#criar tabela usuários, caso não exista
cursor.execute("CREATE TABLE IF NOT EXISTS usuario ( id int not null auto_increment, login VARCHAR(8), senha VARCHAR(4), PRIMARY KEY(id)  )")
print("Tabela criada com sucesso.")

try:
    while True:
        opcao = funcao_cadastro.mostrarMenu()
        if opcao == 1:
            funcao_cadastro.adicionarUsuario(cursor)
            conexao.commit()
        elif opcao == 2:
            funcao_cadastro.verUsuarios(cursor)
        elif opcao == 3:
            funcao_cadastro.checarUsuario(cursor)
        elif opcao == 4:
            funcao_cadastro.excluirBanco(cursor)
            conexao.commit()
            break
        elif opcao == 0:
            break
        else:
            print("Opção inválida.")
    
        print()
        input("Pressione ENTER para retornar ao menu de opções.")

except Exception as erro:
    print(f"Erro: {erro}")

print()
print("Fim do Programa.")
