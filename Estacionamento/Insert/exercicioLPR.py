import mysql.connector, exercicioLPR_funcoes

# Primeira parte: checagem do banco de dados.
# - Você deve pedir para o usuário via input: 
# o host, o user e o password.
print("Iniciando o sistema")
varHost = input("Informe o servidor do BD: ")
varUser = input(f"Informe o usuário do servidor {varHost}: ")
varPass = input(f"Informe a senha do usuário {varUser}: ")

# - Conecte ao banco usando essas informações fornecidas pelo usuário.
try:
    conexao = mysql.connector.connect(
                                        host = varHost,
                                        user = varUser,
                                        password = varPass)
    print(f"Conectado ao servidor {varHost} com sucesso.")
except Exception as erro:
    print(f"Ocorreu o seguinte erro: {erro}")

# - Crie a base LPR (se ainda não existir).
input("Para criar a base de dados, pressione ENTER")
cursor = conexao.cursor()
sql = "CREATE DATABASE IF NOT EXISTS lpra"
try:
    cursor.execute(sql)
    print("Base de dados LPR criada com sucesso no servidor.")
except Exception as erro:
    print(f"Ocorreu o seguinte erro: {erro}")

# SELECIONAR A BASE CRIADA:
conexao.database = "lpra"
print("Base de dados LPR selecionada.")

# - Crie as tabelas (se ainda não existirem) veículos, cruzamentos e leituras.
input("Para criar as tabelas, pressione ENTER")
exercicioLPR_funcoes.criarTabelas(cursor)
conexao.commit()

# - Insira 10 carros (a seu critério).
input("Para inserir os carros, pressione ENTER")
exercicioLPR_funcoes.inserirCarros(cursor)
conexao.commit()

# - Insira 5 cruzamentos (a seu critério).
input("Para inserir os cruzamentos, pressione ENTER")
exercicioLPR_funcoes.inserirCruzamentos(cursor)
conexao.commit()

# Segunda parte: inserção de leituras
while True:
    # - Solicite ao usuário quantas leituras o sistema realizou.
    qtddLeituras = int(input("Informe quantas leituras o sistema realizou: "))
    print("Agora forneca o id do cruzamento e a placa lida para cada leitura:")
    
    exercicioLPR_funcoes.inserirLeituras(cursor,qtddLeituras)
    conexao.commit()

    repetir = input("Deseja continuar fazendo leituras? S|N: ")
    if repetir == "N":
        break

cursor.close()
conexao.close()