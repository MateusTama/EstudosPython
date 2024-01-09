# Exercício 1 Pág 28.

# Lista com 128 nomes. Obrigado Chat GPT! 
nomes = [ 
    "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry",
    "Isabel", "Jack", "Katherine", "Liam", "Mia", "Noah", "Olivia", "Penelope",
    "Quincy", "Rachel", "Samuel", "Sophia", "Thomas", "Ursula", "Victor", "Wendy",
    "Xander", "Yasmine", "Zachary", "Amelia", "Benjamin", "Chloe", "Daniel", 
    "Ella", "Felix", "Gabriella", "Harrison", "Ivy", "Jacob", "Kylie", "Leo", 
    "Mila", "Nathan", "Oscar", "Poppy", "Quinn", "Riley", "Stella", "Theodore", 
    "Ulysses", "Violet", "William", "Xenia", "Yara", "Zane", "Ava", "Bryce", 
    "Cora", "Dylan", "Eva", "Finn", "Giselle", "Hudson", "Isla", "Jasmine", 
    "Kai", "Luna", "Mason", "Nora", "Owen", "Piper", "Qiana", "Reese", "Sofia", 
    "Tristan", "Uma", "Vincent", "Willow", "Xavier", "Yvette", "Zara", "Aaron", 
    "Bella", "Caleb", "Daisy", "Eli", "Freya", "George", "Hazel", "Isaac", 
    "Julia", "Kaiden", "Lily", "Maddox", "Nina", "Oliver", "Penelope", "Quincy", 
    "Ruby", "Sebastian", "Tessa", "Ulysses", "Vera", "Wyatt", "Xander", "Yara", 
    "Zoe", "Axel", "Brielle", "Colton", "Daphne", "Ezra", "Fiona", "Gavin", "Harper",
    "Ian", "Jade", "Kaden", "Lila", "Milo", "Natalie", "Oliver", "Paige", "Quentin", 
    "Rose", "Sawyer", "Taylor", "Uriel", "Valentina", "Wesley"
]

# Ordenar a lista.
nomes.sort() # Ordenando a lista de A-Z = .sort(), Z-A = .reverse(). Ex: nomes.reverse()

def pesquisa_binario(listaBusca, itemRequerido):
    tentativa = 0
    baixo = 0 # Iniciamos a contagem em 0
    alto = len(listaBusca) - 1 # Fim da lista (lista começa em 0, 1, 2...)
    while baixo <= alto: # Algoritmo para no momento em que a média se tornar negativa. Baixo fica com valor maior que o alto. Baixo = meio + 1 maior que o alto. Isso acontece a partir que chegamos no fim da lista e a varíavel baixo incrementa o meio + 1.
        meio = int((baixo + alto) / 2) # Média aritmética da lista (menor e maior número). Convertemos para inteiro.
        tentativa += 1
        print(tentativa)
        chute = listaBusca[meio] # Chute vai ser feito na metade da lista (Busca binária)
        if chute == itemRequerido: # Se acertar o algoritmo retorna o indice do item da busca.
            return meio
        if chute > itemRequerido: # Se o chute for maior que o item requerido a lista é reduzida pela metade - 1
            alto = meio - 1 
        if chute < itemRequerido: # Se o chute for menor que o item requerido a lista agora começa pelo meio + 1
            baixo = meio + 1
    return None # Fim da lista e o item não foi encontrado. Logo ele não existe na lista

print("Resultado:", pesquisa_binario(nomes, "Eli"))

# log 128 na base 2. 128 = 2 elevado a 7. log2^7 na base 2 = 7. Ou seja o número máxima de tentativas vai ser 7