#Busca linear em alocação sequencial

def buscarElemento(lista, elementoBusca):
    indice = 0
    for elemento in lista:
        indice += 1
        if elemento == elementoBusca:
            print(f"Achamos elemento: {elemento}")
            return elemento
    return None
    
def buscarElemento2(lista, indiceBusca):
    #Retorna o indice do elemento se ele estiver na lista, se não estiver retorna None
    for i in range(len(lista)):
        if lista[i] == indiceBusca:
            return i 
    return None

listaNumeros = [3, 7, 29, 95]
print(buscarElemento(listaNumeros, 5))