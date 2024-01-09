#Construindo uma lista encadeada em Python
#Um nó armazena o dado e o endereço do próximo nó

#Node = nó
class Node:
    #data = dado
    def __init__(self, data):
        #declarando o dado e o endereço do próximo nó
        self.data = data
        self.next_node = None

#Testes
        
# node1 = Node("Maça")
# print(f"Node1. Data: {node1.data}. Next Node: {node1.next_node}")

# node2 = Node("Goiaba")
# print(f"Node2. Data: {node2.data}. Next Node: {node2.next_node}")

# #Próximo nó do node1 é o node2
# node1.next_node = node2
# print(node1.next_node) #Informa o próximo nó do node1 e o seu endereço na memória
# print(node1.next_node.data) #Informa o data do node2, a partir do next_node do node1