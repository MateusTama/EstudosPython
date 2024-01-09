import funcoes

nomeArquivo = "urna.txt"
nomeArquivoVoto = "votos.txt"



while True:
    opcaoMenu = funcoes.mostrarMenu()
    if opcaoMenu == 1:
        try:
            listaNumeros = []
            listaVotos = []
            arquivo = open(nomeArquivo, "a")
            nome = input("Digite o nome do candidato: ")
                
            partido = input("Digite o partido do candidato: ")
                
            numero = input("Digite o numero do candidato: ")
            listaNumeros.append(0)
            listaVotos.append(0)

            arquivo.write(f"{nome};{partido};{numero}\n")
            arquivo.close()
        except:
            print("Erro...")
        else:    
            print("Arquivo atualizado com sucesso.")
    elif opcaoMenu == 2:
        funcoes.listarCadastros(nomeArquivo)
    elif opcaoMenu == 3:
        funcoes.atualizarCadastro(nomeArquivo)
    elif opcaoMenu == 4:
        funcoes.removerCadastro(nomeArquivo)
    elif opcaoMenu == 5:
        funcoes.listarCadastros(nomeArquivo)        
        funcoes.votar(nomeArquivo,nomeArquivoVoto,listaNumeros,listaVotos)
    elif opcaoMenu == 0:
        break

funcoes.Vencedor
print("Programa encerrado.")


