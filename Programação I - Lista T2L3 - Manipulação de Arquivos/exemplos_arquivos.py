import funcoes

nomeArquivo = "dados.txt"

while True:
    opcaoMenu = funcoes.mostrarMenu()
    if opcaoMenu == 1:
        funcoes.novoCadastro(nomeArquivo)
    elif opcaoMenu == 2:
        funcoes.listarCadastros(nomeArquivo)
    elif opcaoMenu == 3:
        funcoes.atualizarCadastro(nomeArquivo)
    elif opcaoMenu == 4:
        funcoes.removerCadastro(nomeArquivo)
    elif opcaoMenu == 0:
        break

print("Programa encerrado.")

