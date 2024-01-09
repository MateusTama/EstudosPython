import cadastro_funcoes


escolha = cadastro_funcoes.mostrarMenu()

while escolha != 6:
    if escolha == 1:
        cadastro_funcoes.usuarios()
    elif escolha == 2:
        cadastro_funcoes.verificar_usuario()
    elif escolha == 3:
         cadastro_funcoes.listar_usuarios()

    escolha = cadastro_funcoes.mostrarMenu()

print("Programa encerrado.")