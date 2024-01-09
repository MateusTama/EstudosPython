# biblioteca necessária para trabalhar com mysql
import mysql.connector

try:
    # abrir conexão com o banco 
    conexao = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="")
    print("Conectado com sucesso ao servidor de banco de dados.")
except Exception as erro:
    print(f"Erro na conexão com o banco de dados: {erro}")

# objeto que envia os comandos para a conexão aberta
cursor = conexao.cursor()
try:
    # função que manda os comandos para a conexão
    cursor.execute("CREATE DATABASE IF NOT EXISTS 2infoA")
    print("Base criada com sucesso.")

    # selecionar a database
    conexao.database = "2infoa"

    cursor.execute("CREATE TABLE alunos ( id int, nome VARCHAR(45), PRIMARY KEY(id)  )")
    print("Tabela ALUNOS criada com sucesso.")
    # função que garante a execução dos comandos dentro do banco
    conexao.commit()
except Exception as erro:
    print(f"Erro ao enviar o comando sql: {erro}")

# garantir o encerramento da conexão para evitar problemas
cursor.close()
conexao.close()