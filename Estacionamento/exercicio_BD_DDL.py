import mysql.connector

# escreva uma função que receba o nome da tabela e a lista de campos 
# por parâmetro, e retorne o comando SQL completo de criação da tabela.
def geraSQL(parNomeTabela, parListaCampos):
    sql = f"CREATE TABLE {parNomeTabela} (id int AUTO_INCREMENT, "
    for campo in parListaCampos:
        sql = sql + f"{campo} VARCHAR(50) ,"

    sql = sql + " PRIMARY KEY (id) )"
    return sql
###########################################################################



# Você deve pedir para o usuário via input: o host, o user e o password.
servidor = input("Informe o endereço do servidor do banco de dados: ")
usuario = input(f"Informe o usuário do servidor {servidor}: ")
senha = input(f"Informe a senha do usuário {usuario}: ")

#Conecte ao banco usando essas informações fornecidas pelo usuário.
try:
    conexao = mysql.connector.connect(
                                host=servidor,
                                user=usuario,
                                password=senha)
    input("Conectado com sucesso ao banco de dados. Pressione ENTER.")
except Exception as erro:
    print(f"Erro de conexão: {erro}")

# Solicite ao usuário qual o nome da base que deve ser criada. 
# Crie essa base via python.
base = input("Qual o nome da base que você vai criar? ")

cursor = conexao.cursor()
try:
    if conexao.is_connected():
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {base}")
        print(f"Base {base} criada com sucesso.")
        # Se criar com sucesso, não esqueça de selecionar 
        # ela para poder criar a tabela depois.
        conexao.database = base
    else:
        print("A conexão com o banco de dados foi interrompida!")
except Exception as erro:
    print(f"Erro: {erro}")

# Solicite ao usuário o nome da tabela que ele deseja criar, 
# e pergunte quantos campos essa tabela deve ter.
nomeTabela = input("Qual o nome da tabela que você deseja criar? ")
quantosCampos = int(input(f"Quantos campos a tabela {nomeTabela} terá? "))

# Faça uma repetição com a quantidade de campos informada, 
# e pergunte ao usuário o nome de cada campo. 
# Adicione o nome de cada campo em uma lista.
listaCampos = []
for campo in range(quantosCampos):
    nomeCampo = input(f"Qual o nome do campo {campo+1}? ")
    listaCampos.append(nomeCampo)

# No programa principal, chame a função passando os parâmetros 
# corretos, e pegue o retorno dela em uma variável.
sql = geraSQL(nomeTabela, listaCampos)

####### TESTE TESTE TESTE TESTE #######
# input(sql)
####### TESTE TESTE TESTE TESTE #######


# Execute o comando SQL retornado pela função para criar a tabela.
try:
    if conexao.is_connected():
        cursor.execute(sql)
        print(f"Tabela {nomeTabela} criada com sucesso.")
    else:
        print("A conexão com o banco de dados foi interrompida!")
except Exception as erro:
    print(f"Erro: {erro}")

cursor.close()
conexao.close()