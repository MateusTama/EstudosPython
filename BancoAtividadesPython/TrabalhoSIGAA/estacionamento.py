import mysql.connector 
from funcoes import *

conexao = conectarBancoDados()
cursor = conexao.cursor()

while True:
    opcao = mostrarMenu()

    if opcao == 1:
        verEstacionamento(cursor,0)
    elif opcao == 2:
        escolherPavimento(cursor)
    elif opcao == 3:
        checarVaga(cursor)
    elif opcao == 4:
        alterarVaga(cursor)
        conexao.commit()
    elif opcao == 5:
        esvaziarEstacionamento(cursor)
        conexao.commit()
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")

    print()
    input("Pressione ENTER para retornar ao menu.")
