# Algoritmo de ordenação
# Tempo de execução O(n^2) = O(n x n)

# Ordenar array do menor para o maior

# Arrays devem ser do mesmo tipo: int, str, booleans

def buscaMenor(array):
    menor = array[0]
    menor_indice = 0
    for indice_elemento in range(1, len(array)):
        if array[indice_elemento] < menor:
            menor = array[indice_elemento]
            menor_indice = indice_elemento
    return menor_indice

def ordenaçãoSeleção(array):
    novoArray = []
    for elemento in range(1, len(array)+1):
        menor = buscaMenor(array)
        novoArray.append(array.pop(menor))
    return novoArray

print(ordenaçãoSeleção([10, 15, 5, 6, 1, 0, 3, 27]))