#Algoritmo = Conjunto de instruções que realiza uma tarefa. Trecho de código. 

# Função de pesquisa binária - Algoritmos.

# Pesquisa binária. Algumas considerações:
# - A lista precisa estar ordenada.
# - log n na base 2

# Pesquisa Simples:
# - n etapas

# 240.000 mil tentativas x 18 tentativas

def pesquisa_binario(listaBusca, itemRequerido):
    baixo = 0 # Iniciamos a contagem em 0
    alto = len(listaBusca) - 1 # Fim da lista (lista começa em 0, 1, 2...)
    while baixo <= alto: # Algoritmo para no momento em que a média se tornar negativa. Baixo fica com valor maior que o alto. Baixo = meio + 1 maior que o alto. Isso acontece a partir que chegamos no fim da lista e a varíavel baixo incrementa o meio + 1.
        meio = int((baixo + alto) / 2) # Média aritmética da lista (menor e maior número). Convertemos para inteiro.
        meioSemInt = (baixo + alto) / 2
        print(meio)
        print(meioSemInt)
        chute = listaBusca[meio] # Chute vai ser feito na metade da lista (Busca binária)
        if chute == itemRequerido: # Se acertar o algoritmo retorna o indice do item da busca.
            return meio
        if chute > itemRequerido: # Se o chute for maior que o item requerido a lista é reduzida pela metade - 1
            alto = meio - 1 
        if chute < itemRequerido: # Se o chute for menor que o item requerido a lista agora começa pelo meio + 1
            baixo = meio + 1
    return None # Fim da lista e o item não foi encontrado. Logo ele não existe na lista

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] # Lista de números

print(pesquisa_binario(lista, 20)) #Na listaBusca ele vai procurar o 20, caso esse esteja presente retornamos o seu indice. Caso contrário retornamos o None e o item não foi encontrado

# Tempo de execução logarítmica x Tempo de execução linear.