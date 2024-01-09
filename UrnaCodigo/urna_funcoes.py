
from posixpath import split


def urnaMenu():
    print()
    print("1. Cadastrar candidato")
    print("2. Listar candidato")
    print("3. Alterar candidato")
    print("4. Remover candidato")
    print("5. Iniciar votação")
    print("0. Sair")
    print()
    escolha = int(input("Escolha uma opção: "))
    return escolha

def UrnaCadastro(parUrna):

    print()
    arquivo = open(parUrna, "a")
    nome = input("Informe seu nome: ")
    partido = input("Informe seu partido: ")
    numero = input("Informe seu número: ")
    arquivo.write(f"{nome};{partido};{numero}\n")
    arquivo.close()

def ListarCandidato(parUrna):

    arquivo = open(parUrna, "r")
    print("...")
    print()

    for linha in arquivo:
        DadosLista = linha.split(";")
        nome = DadosLista[0]
        partido = DadosLista[1]
        numero = DadosLista[2].strip()

        print(f"Nome: {nome} | Partido: {partido} | Número: {numero}")

    arquivo.close()

def AlterarCandidato(parUrna):

    print()
    arquivo = open(parUrna, "r")
    atualizado = ""
    buscar = input("Digite o numero do candidato a ser alterado: ")
    for linha in arquivo:
        DadosLista = linha.split(";")
        nome = DadosLista[0]
        partido = DadosLista[1]
        numero = DadosLista[2].strip()
        if numero == buscar:
            print()
            print("Alterar...")
            print()
            nome = input("Insira o novo nome: ")
            partido = input("Insira o novo nome partido: ")
            numero = input("Insira o novo numero: ")
        atualizado += f"{nome};{partido};{numero}\n"
    arquivo.close()
    arquivo = open(parUrna, "w")
    arquivo.write(atualizado)
    arquivo.close()

def RemoverCandidato(parUrna):
    
    print()
    arquivo = open(parUrna, "r")
    atualizado = ""
    buscar = input("Qual candidato você deseja remover - Escreva seu número de campanha - : ")
    for linha in arquivo:
        DadosLista = linha.split(";")
        nome = DadosLista[0]
        partido = DadosLista[1]
        numero = DadosLista[2].strip()
        if numero != buscar:
            atualizado += f"{nome};{partido};{numero}\n"
    arquivo.close()
    arquivo = open(parUrna, "w")
    arquivo.write(atualizado)
    arquivo.close()

def IniciarVotacao(parUrna, parVota):
    
    print()
    print("Iniciando votação...")
    print()

    arquivo = open(parUrna, "r")
    arquivoVota = open(parVota, "a")
    
    sair = ""
    numVotos = 1
    while sair != "s":
        voto = ""
       
        numVotacao = input("Insira o numero do seu candidato: ")
        for linha in arquivo:
            DadosLista = linha.split(";")
            nome = DadosLista[0]
            partido = DadosLista[1]
            numero = DadosLista[2].strip()
            print(f"Nome: {nome} \nPartido: {partido} \nNumero: {numero} \n")
            if numVotacao == numero:
                numVotos += 1
                voto += f"{numVotacao};{numVotos}\n"
            arquivoVota.write(voto)

        print()

        sair = input("Deseja finalizar as votações? s/n : ")

    arquivo.close() 
    arquivoVota.close()

    #arquivoVota = open(parVota, "a")





    #qntVotos = 0
    #continuar = ""
    #while continuar != "n":
        #armVotos = ""
        #part = ""
        #numCand = 0
        #nome = DadosLista[0]
        #partido = DadosLista[1]
        #numero = DadosLista[2]
        #part = input("Informe o partido do candidato: ")
        #print()
        #numCand = input("Informe o número do candidato: ")
        #print()
        #if numero == numCand and partido == part:
            #qntVotos += 1
            #armVotos += f"{qntVotos}\n"
            #arquivoVota.write(armVotos)
            
        #print()
        #continuar = input("Você deseja continuar a votação? s/n : ")

    #arquivoVota.close()
    #arquivo.close()
            


    






        

    


        
            





    




    






