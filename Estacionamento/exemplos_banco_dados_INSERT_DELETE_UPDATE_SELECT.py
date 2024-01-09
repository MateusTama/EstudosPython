import mysql.connector, pandas

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="2info")
    print("Conectado ao banco de dados com sucesso.")
except Exception as erro:
    print(erro)

cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS produtos (
                                    id INT NOT NULL AUTO_INCREMENT, 
                                    descricao VARCHAR(40), 
                                    valor_unit DOUBLE, 
                                    quantidade INT, 
                                    PRIMARY KEY(id)
                                    );"""
try:
    cursor.execute(sql)
    print("Tabela criada com sucesso.")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
conexao.commit()

# # INSERT
# descricao = input("Informe a descrição do produto: ")
# valor = input("Informe o valor unitário desse produto: ")
# quantidade = input("Informe a quantidade de estoque do novo produto:" )
# sql = f"""  INSERT INTO produtos 
#                             (descricao, valor_unit, quantidade) 
#                         VALUES 
#                             ('{descricao}',{valor},{quantidade})
#                 """
# try:
#     cursor.execute(sql)
#     print("Registro inderido com sucesso.")
#     conexao.commit()

# except Exception as erro:
#     print(erro)

# # DELETE
# codigo = input("Informe o código do produto a ser deletado: ")
# sql = f"DELETE FROM produtos WHERE id = {codigo}"
# try:
#     cursor.execute(sql)
#     print("Rsgistro deletado com sucesso.")
#     conexao.commit()

# except Exception as erro:
#     print(erro)

# # UPDATE
# codigo = input("Informe o código do produto a ser atualizado: ")
# descricao = input("Informe a nova descrição para o produto: ")
# valor = input("Informe o novo valor unitário desse produto: ")
# quantidade = input("Informe a nova quantidade de estoque do novo produto:" )
# sql = f"""UPDATE produtos SET
#                     descricao = '{descricao}',
#                     valor_unit = {valor},
#                     quantidade = {quantidade}
#                 WHERE id = {codigo}"""
# try:
#     cursor.execute(sql)
#     conexao.commit()

# except Exception as erro:
#     print(erro)

# # SELECT (buscar somente um registro; resultados sem PANDAS)
# produto = input("Informe o nome do produto para buscar: ")
# sql = f"SELECT * FROM produtos WHERE descricao = '{produto}'"
# try:
#     cursor.execute(sql)
#     resultado = cursor.fetchall()
#     for linha in resultado:
#         print("id:",linha[0])
#         print("descrição:",linha[1])
#         print("valor:",linha[2])
#         print("quantidade:",linha[3])

# except Exception as erro:
#     print(erro)



# # SELECT (buscar todos os registros; resultados com PANDAS)
# sql = "SELECT * FROM produtos"
# try:
#     cursor.execute(sql)
#     resultado = pandas.DataFrame( cursor.fetchall() )
#     print(resultado.to_markdown())

# except Exception as erro:
#     print(erro)


cursor.close()
conexao.close()