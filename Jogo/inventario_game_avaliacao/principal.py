import classesGame
# ESSE ARQUIVO É APENAS UM EXEMPLO DE COMO USAR AS CLASSES
# SEU CONTEÚDO DEVE SER APAGADO PARA SEGUIR O ROTEIRO DA AVALIAÇÃO 
# AS INSTRUÇÕES ESTÃO POSTADAS NO SIGAA
#  
nome = input("Qual o nome? ")
categoria = input("Qual a categoria? ")
jogador = classesGame.Player(nome, categoria)

nome = jogador.obterNome() 
print(nome)

dinheiro = jogador.obterDinheiro()
print(dinheiro)

capacidadeInventario = jogador.inventario.obterCapacidade()
print(capacidadeInventario)

novoItem = classesGame.Item("Arco","Arma que atira flechas",100,1)
jogador.inventario.adicionarItem(novoItem)

novoItem2 = classesGame.Item("Laranja","Comida que aumenta a vida",5,3)
jogador.inventario.adicionarItem(novoItem2)

jogador.inventario.mostrarInventario()

jogador.inventario.descartarItem()
jogador.inventario.mostrarInventario()