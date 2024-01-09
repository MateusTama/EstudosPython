import mysql.connector

def conectarBancoDados():
    print("Informe as seguintes informações para conexão com banco de dados:")
    host = input("Informe o host(ex:localhost): ")
    user = input("Informe o usuário(ex: root): ")
    password = input("Informe a sua senha(ex: ifcbrusque): ")

    try:
        conexao = mysql.connector.connect(
                                    host=host,
                                    user=user,
                                    password=password,
                                    database="estacionamento")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        return conexao

def mostrarMenu():
    print()
    print("Selecione a opção desejada:")
    print()
    print("1 - Ver a situação do estacionamento.")
    print("2 - Escolhar um pavimento.")
    print("3 - Checar a situação da vaga.")
    print("4 - Alterar situação da vaga.")
    print("5 - Esvaziar estacionamento.")
    print("0 - Sair")
    print()
    resposta = int(input("Número da sua opção: "))
    print()
    return resposta

def verEstacionamento(parCursor, parPavimento):
    sql = "SELECT * FROM vagas, pavimentos WHERE vagas.id_pavimento = pavimentos.id"
    if parPavimento != 0:
        sql += f" AND pavimentos.id = '{parPavimento}'"        

    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    
    for linha in tabelaSelect:
        ocupado = "[X]" if linha[3] else "[ ]"
        print(f"{ocupado} Vaga: {linha[0]} Vaga do Pavimento: {linha[2]} Pavimento: {linha[1]} - {linha[5]}")

def escolherPavimento(parCursor):
    sql = "SELECT * FROM pavimentos"
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    print("Códigos dos pavimentos:\n")
    for linha in tabelaSelect:
        print(f"{linha[0]} - {linha[1]}")
    print()
    codigoPavimento = input("Informe o código do pavimento desejado: ")
    print()
    verEstacionamento(parCursor, codigoPavimento)

def checarVaga(parCursor):
    idPavimento = input("Informe o código do pavimento: ")
    vaga = int(input("Informe o código da vaga: "))
    sql = f"SELECT * FROM vagas, pavimentos WHERE id_pavimento = '{idPavimento}' AND numero = {vaga} AND vagas.id_pavimento = pavimentos.id"    
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    print()
    if len(tabelaSelect) == 0:
        print("Código inválido.")
    else:
        linha = list(tabelaSelect[0])
        ocupado = "ocupada" if linha[3] else "livre"
        print(f"Vaga do Pavimento: {linha[2]}. Pavimento: {linha[1]} - {linha[5]}")
        print(f"Essa vaga está {ocupado}.")

def alterarVaga(parCursor):
    sql = "SELECT * FROM vagas, pavimentos WHERE vagas.id_pavimento = pavimentos.id"
    parCursor.execute(sql)
    tabelaSelect = parCursor.fetchall()
    vagaLivre = []
    for linha in tabelaSelect:
        ocupado = "[X]" if linha[3] else "[ ]"
        print(f"{ocupado} Código da Vaga: {linha[0]} Vaga do Pavimento: {linha[2]} Pavimento: {linha[1]} - {linha[5]}")
        if(ocupado == "[ ]"):
            vagaLivre.append(linha[0])

    print()
    estacionar = int(input("Qual o código da vaga que você deseja estacionar: "))
    for item in vagaLivre:
        vaga = int(item)
        if vaga == estacionar:
            sql = f"UPDATE vagas SET ocupada = 1 WHERE id = '{estacionar}'"
            parCursor.execute(sql)
            break

def esvaziarEstacionamento(parCursor):
    resposta = input("Tem certeza que deseja esvaziar o estacionamento - (s/n) - : ")
    if resposta == "s":
        sql = "UPDATE vagas SET ocupada = 0"
        parCursor.execute(sql)
        print("Estacionamento esvaziado.")
    else:
        print("Compreensível.")