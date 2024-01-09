def mostrarMenu():
    print()
    print("Menu:")
    print("1. Novo Cadastro")
    print("2. Listar Cadastros")
    print("3. Atualizar Cadastro")
    print("4. Remover Cadastro")
    print("0. Sair")
    escolha = int(input("Digite o número da opção desejada:"))
    print()

    return escolha

def novoCadastro(parNomeArquivo):
    try:
        # abrir o arquivo no modo "append" para adicionar conteúdo
        arquivo = open(parNomeArquivo, "a")
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        # escrever uma linha no arquivo usando os dados digitados 
        # separados por ";"
        arquivo.write(f"{nome};{email};{telefone}\n")
        arquivo.close()
    except:
        print("Erro...")
    else:
        print("Arquivo atualizado com sucesso.")
        
def listarCadastros(parNomeArquivo):
    try:

        # abrir o arquivo no modo "read"
        arquivo = open(parNomeArquivo,"r")
        print()
        print("Início da Lista:")
        print()

        for linha in arquivo:
            # separar os dados do conteúdo usando o ";"
            # gera uma lista com os dados separados
            lista_dados = linha.split(";")
            # organizar os dados da lista em variáveis separadas
            nome = lista_dados[0]
            email = lista_dados[1]
            telefone = lista_dados[2].strip()

            # montar a frase na tela
            print(f"Nome: {nome} / E-mail: {email} / Telefone: {telefone}")

        arquivo.close()    
    except:
        print("Erro...")
    else:
        print()
        print("Fim do arquivo.")

def atualizarCadastro(parNomeArquivo):
    try:
        # abrir o arquivo no modo "read"
        arquivo = open(parNomeArquivo,"r")
        # variável que va receber o conteudo atualizado 
        # para ser reescrito no arquivo
        conteudoNovo = ""
        
        # perguntar qual cadastro precisa ser alterado
        busca = input("Digite o email do cadastro a alterar:")

        for linha in arquivo:
            # separar os dados do conteúdo usando o ";"
            # gera uma lista com os dados separados
            lista_dados = linha.split(";")
            # organizar os dados da lista em variáveis separadas
            nome = lista_dados[0]
            email = lista_dados[1]
            telefone = lista_dados[2].strip()
            # verifica se essa linha é a que precisa ser alterada
            if email == busca:
                # se for, pede as novas informações
                nome = input("Novo Nome: ")
                email = input("Novo E-mail: ")
                telefone = input("Novo Telefone: ") 
            # guarda a linha na variável que vai atualizar o arquivo
            conteudoNovo += f"{nome};{email};{telefone}\n"
        # fecha o arquivo que estava somente leitura
        arquivo.close()    
        # abre novamente mas agora em modo "write"
        arquivo = open(parNomeArquivo, "w")
        # agora que o arquivo está zerado, escrevemos o conteúdo atualizado
        arquivo.write(conteudoNovo)
        arquivo.close()

    except:
        print("Erro...")
    else:
        print()
        print("Atualização efetivada com sucesso.")

def removerCadastro(parNomeArquivo):
    try:
        # abrir o arquivo no modo "read"
        arquivo = open(parNomeArquivo,"r")
        # variável que va receber o conteudo atualizado 
        # para ser reescrito no arquivo
        conteudoNovo = ""
        
        # perguntar qual cadastro precisa ser alterado
        busca = input("Digite o email do cadastro a remover:")

        for linha in arquivo:
            # separar os dados do conteúdo usando o ";"
            # gera uma lista com os dados separados
            lista_dados = linha.split(";")
            # organizar os dados da lista em variáveis separadas
            nome = lista_dados[0]
            email = lista_dados[1]
            telefone = lista_dados[2].strip()
            # verifica se essa linha é a que precisa ser alterada
            if email != busca:
                # guarda a linha na variável que vai atualizar o arquivo
                conteudoNovo += f"{nome};{email};{telefone}\n" 
            
        # fecha o arquivo que estava somente leitura
        arquivo.close()    
        # abre novamente mas agora em modo "write"
        arquivo = open(parNomeArquivo, "w")
        # agora que o arquivo está zerado, escrevemos o conteúdo atualizado
        arquivo.write(conteudoNovo)
        arquivo.close()

    except:
        print("Erro...")
    else:
        print()
        print("Cadastro removido com sucesso.")