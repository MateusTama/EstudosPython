def mostrarMenu():
    print()
    print("Menu:")
    print("1. Novo Cadastro")
    print("2. Listar Cadastros")
    print("3. Atualizar Cadastro")
    print("4. Remover Cadastro")
    print("5. Votar")
    print("0. Sair")
    escolha = int(input("Digite o número da opção desejada:"))
    print()

    return escolha
        
def listarCadastros(parNomeArquivo):
    try:

        arquivo = open(parNomeArquivo,"r")
        print()
        print("Início da Lista:")
        print()

        for linha in arquivo:
            lista_dados = linha.split(";")
            nome = lista_dados[0]
            partido = lista_dados[1]
            numero = lista_dados[2].strip()

            print(f"Nome: {nome} / Partido: {partido} / Numero: {numero}")

        arquivo.close()    
    except:
        print("Erro...")
    else:
        print()

def atualizarCadastro(parNomeArquivo):
    try:
        arquivo = open(parNomeArquivo,"r")
        conteudoNovo = ""
        
        busca = input("Digite o partido do cadastro a alterar:")

        for linha in arquivo:
            lista_dados = linha.split(";")
            nome = lista_dados[0]
            partido = lista_dados[1]
            numero = lista_dados[2].strip()
            if partido == busca:
                nome = input("Novo Nome: ")
                partido = input("Novo Partido: ")
                numero = input("Novo Numero: ") 
            conteudoNovo += f"{nome};{partido};{numero}\n"
        arquivo.close()    
        arquivo = open(parNomeArquivo, "w")
        arquivo.write(conteudoNovo)
        arquivo.close()

    except:
        print("Erro...")
    else:
        print()
        print("Atualização efetivada com sucesso.")

def removerCadastro(parNomeArquivo):
    try:
        arquivo = open(parNomeArquivo,"r")
        conteudoNovo = ""
        
        busca = input("Digite o partido do cadastro a remover:")

        for linha in arquivo:
            lista_dados = linha.split(";")
            nome = lista_dados[0]
            partido = lista_dados[1]
            numero = lista_dados[2].strip()
            if partido != busca:
                conteudoNovo += f"{nome};{partido};{numero}\n" 
            
        arquivo.close()    
        arquivo = open(parNomeArquivo, "w")
        arquivo.write(conteudoNovo)
        arquivo.close()

    except:
        print("Erro...")
    else:
        print()
        print("Cadastro removido com sucesso.")


def Vencedor(parNomeArquivo):

        arquivo = open(parNomeArquivo,"r")
        print()
        print("Candidatos:")
        print()

        for linha in arquivo:

            lista_dados = linha.split(";")
            nome = lista_dados[0]
            partido = lista_dados[1]
            numero = lista_dados[2].strip()

            print(f"Nome: {nome} / Partido: {partido} / Numero: {numero}")

        arquivo.close()    

def votar(parNomeArquivo, parNomeArquivoVoto,parListaNumeros,parListaVotos):
        arquivo = open(parNomeArquivo,"r")
        arquivoVoto = open(parNomeArquivoVoto,"w")
        conteudoNovo = ""
        pergunta = "s"

        while(pergunta == "s"):
            buscar = input("Digite o úmero do candidato que você quer votar:")
            for linha in arquivo:
                lista_dados = linha.split(";")
                numero = lista_dados[0]
                votos = lista_dados[1].strip()
                numeroVotos = 0
                indiceNumero = 0
                if numero == buscar:
                    indiceNumero = parListaNumeros.index(numero)
                    numeroVotos = parListaVotos[indiceNumero] + 1
                    parListaVotos.insert(indiceNumero,numeroVotos)
                    votos = parListaVotos[indiceNumero]

                conteudoNovo += f"{numero};{votos}\n"
            arquivoVoto.write(conteudoNovo)
            pergunta = input("Deseja votar novamente?s/n: ")
        else:
            arquivo.close()  
            arquivoVoto.close()
            #arquivoVoto = open(parNomeArquivoVoto, "w")
            #arquivoVoto.write(conteudoNovo)
            #arquivoVoto.close()


