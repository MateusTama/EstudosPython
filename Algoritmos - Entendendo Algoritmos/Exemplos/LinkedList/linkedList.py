from node import Node

#Criando as listas encadeadas
#Uma lista encadeada deve ter a mesma interface útil que uma lista sequencial (memória sequencialmente alocada x memória dinamicamente alocada)

class LinkedList:
    #Constructor sem parâmetros
    def __init__(self):
        #2 atributos. Head, o "primeiro" nó que vai indicar o nó subsequente. Size, para mensurar o tamanho de uma lista vazia, útil para testes.
        self.head = None
        self._size = 0

    #Método para adicionar elementos na lista (node)
    def append(self, element):
        #Lista já possui o primeiro nó. Head.
        if self.head:
            pointer = self.head
            #Loop while para verificar todos os nós da lista a partir do head. "Pointer".
            #Enquanto os nós estiverem apontando para outro nó o loop continua. 
            while (pointer.next_node):
                #Variável pointer vai salvar o último nó, que não aponta para nenhum próximo nó
                pointer = pointer.next_node
            #Adicionamos um nó subsequente ao último nó encontrado pelo loop while
            pointer.next_node = Node(element)

        else:
            # primeira inserção e criação do head. Primeiro nó.
            self.head = Node(element)

        #Incrementando 1 ao tamanho da lista, após adicionar 1 elemento
        self._size = self._size + 1

    #Criando um método len para a lista
    def __len__(self):
        # Retorna o tamanho da lista
        return self._size

lista = LinkedList()
# print(lista.size)

lista.append(10)
print(lista._size)
print()