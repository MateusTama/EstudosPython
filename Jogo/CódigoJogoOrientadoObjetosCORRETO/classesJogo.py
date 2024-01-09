#Trabalho feito por Mateus Tamasia, Eduardo Kohler e Lucas da Silva Valim

import random
from statistics import quantiles

class Player:
    def __init__(self, parNome, parCategoria):
        self.__nome = parNome
        self.__categoria = parCategoria
        self.__vida = 100
        self.inventario = Inventory(11)

    def obterNome(self):
        return self.__nome
    
    def alterarNome(self, parNome):
        self.__nome = parNome

    def obterCategoria(self):
        return self.__categoria

    def alterarCategoria(self, parCategoria):
        self.__categoria = parCategoria

    def obterVida(self):
        return self.__vida

    def alterarVida(self, parValor):
        if (self.__vida + parValor) < 0:
            self.__vida = 0
        elif (self.__vida + parValor) > 100:
            self.__vida = 100
        else:
            self.__vida += parValor

class Item:
    def __init__(self, parNome, parDescricao, parValor, parQuantidade):
        self.__nome = parNome
        self.__descricao = parDescricao
        self.__valor = parValor
        self.__quantidade = parQuantidade

    def obterNome(self):
        return self.__nome

    def alterarNome(self, parNome):
        self.__nome = parNome

    def obterDescricao(self):
        return self.__descricao

    def alterarDescricao(self, parDescricao):
        self.__descricao = parDescricao

    def obterValor(self):
        return self.__valor

    def alterarValor(self, parValor):
        self.__valor = parValor

    def obterQuantidade(self):
        return self.__quantidade

    def alterarQuantidade(self, parQuantidade):
        self.__quantidade = parQuantidade

    def mostrar(self):
        print(f"Nome: {self.__nome}")
        print(f"Descrição: {self.__descricao}")
        print(f"Valor: {self.__valor}")
        print(f"Quantidade: {self.__quantidade}")

class Inventory:
    def __init__(self, parCapacidade):
        self.__capacidade = parCapacidade
        self.__itens = []
        self.__comida = []
        self.__protecao = []
        self.__barrinha = []
        self.__maca = []
        self.__pocao = []
        self.__sopaCogumelo = []
        self.__bife = []
    
    def obterCapacidade(self):
        return self.__capacidade

    def alterarCapacidade(self, parCapacidade):
        self.__capacidade = parCapacidade

    def adicionarItem(self, parItem):
        quantidade = len(self.__itens)
        if self.__capacidade > quantidade:
            self.__itens.append(parItem)
        else:
            print("Inventário cheio. Impossível adicionar.")

    def mostrarInventario(self):
        indice = 0
        for meuItem in self.__itens:
            print(f"\nItem {indice+1}:")
            meuItem.mostrar()
            indice += 1

    def adicionarItemComida(self, parItem):
        self.__comida.append(parItem)

    def mostrarInventarioComida(self):
        indice = 0
        for meuItemComida in self.__comida:
            print(f"\nItem {indice+1}:")
            meuItemComida.mostrar()
            indice += 1

    def descartarItem(self):
        self.mostrarInventario()
        print("Para descartar um item, use o índice correspondente:\n")
        indiceRemover = int(input("Digite o número do item a remover: "))-1
        quantidade = len(self.__itens)
        if indiceRemover < quantidade:
            self.__itens.pop(indiceRemover)
            return indiceRemover
        else:
            print("Item inválido.")

    def usarItem(self, parNomeItem):
        indice = 0
        for item in self.__itens:
            nomeDoItem = item.obterNome()
            regenerar = item.obterValor()
            if nomeDoItem == parNomeItem:
                self.__itens.pop(indice)
                return regenerar
                break
            indice += 1

    def usarComida(self, parNomeItem):
        indice = 0
        for item in self.__comida:
            nomeDoItem = item.obterNome()
            if nomeDoItem == parNomeItem:
                self.__comida.pop(indice)
                break
            indice += 1

    def usarChave(self):
        self.__itens.pop(8)

    def quantidadeComida(self):
        quantidade_comida = len(self.__comida)
        return quantidade_comida

    def adicionarItemProtecao(self, parItem):
            self.__protecao.append(parItem)

    def mostrarInventarioProtecao(self):
        indice = 0
        for meuItemProtecao in self.__protecao:
            print(f"\nItem {indice+1}:")
            meuItemProtecao.mostrar()
            indice += 1
    
    def usarProtecao(self, parNomeItem):
        indice = 0
        for item in self.__protecao:
            nomeDoItem = item.obterNome()
            if nomeDoItem == parNomeItem:
                self.__protecao.pop(indice)
                break
            indice += 1

    def quantidadeProtecao(self):
        quantidade_protecao = len(self.__protecao)
        return quantidade_protecao

    def adicionarItemBarrinha(self, parItem):
            self.__barrinha.append(parItem)

    def mostrarInventarioBarrinha(self):
        indice = 0
        for meuItemBarrinha in self.__barrinha:
            print(f"\nItem {indice+1}:")
            meuItemBarrinha.mostrar()
            indice += 1
    
    def usarBarrinha(self, parNomeItem):
        indice = 0
        for item in self.__barrinha:
            nomeDoItem = item.obterNome()
            if nomeDoItem == parNomeItem:
                self.__barrinha.pop(indice)
                break
            indice += 1

    def quantidadeBarrinha(self):
        quantidade_barrinha = len(self.__barrinha)
        return quantidade_barrinha

    def descartarBarrinha(self):
        self.__barrinha.pop(0)
        self.__comida.pop(4)
    
    def descartarAnel(self):
        self.__protecao.pop(0)

    def descartarAmuleto(self):
        self.__protecao.pop(1)
    
    #MAÇA 

    def adicionarItemMaca(self, parItem):
        self.__maca.append(parItem)

    def mostrarInventarioMaca(self):
        indice = 0
        for meuItemMaca in self.__maca:
            print(f"\nItem {indice+1}:")
            meuItemMaca.mostrar()
            indice += 1
    
    def usarMaca(self, parNomeItem):
        indice = 0
        for item in self.__maca:
            nomeDoItem = item.obterNome()
            if nomeDoItem == parNomeItem:
                self.__maca.pop(indice)
                break
            indice += 1

    def descartarMaca(self):
        self.__comida.pop(0)
        self.__maca.pop(0)

    def quantidadeMaca(self):
        quantidade_maca = len(self.__maca)
        return quantidade_maca

    #POÇÃO

    def adicionarItemPocao(self, parItem):
        self.__pocao.append(parItem)

    def mostrarInventarioPocao(self):
        indice = 0
        for meuItemPocao in self.__pocao:
            print(f"\nItem {indice+1}:")
            meuItemPocao.mostrar()
            indice += 1
    
    def usarPocao(self, parNomeItem):
        indice = 0
        for item in self.__pocao:
            nomeDoItem = item.obterNome()
            if nomeDoItem == parNomeItem:
                self.__pocao.pop(indice)
                break
            indice += 1
        
    def descartarPocao(self):
        self.__comida.pop(1)
        self.__pocao.pop(0)

    def quantidadePocao(self):
        quantidade_pocao = len(self.__pocao)
        return quantidade_pocao

    #BIFE

    def adicionarItemBife(self, parItem):
        self.__bife.append(parItem)

    def mostrarInventarioBife(self):
        indice = 0
        for meuItemBife in self.__bife:
            print(f"\nItem {indice+1}:")
            meuItemBife.mostrar()
            indice += 1
    
    def usarBife(self, parNomeItem):
        indice = 0
        for item in self.__bife:
            nomeDoItem = item.obterNome()
            if nomeDoItem == parNomeItem:
                self.__bife.pop(indice)
                break
            indice += 1
    
    def descartarBife(self):
        self.__comida.pop(2)
        self.__bife.pop(0)

    def quantidadeBife(self):
        quantidade_bife = len(self.__bife)
        return quantidade_bife
    
    #SOPA COGUMELO

    def adicionarItemSopaCogumelo(self, parItem):
            self.__sopaCogumelo.append(parItem)

    def mostrarInventarioSopaCogumelo(self):
        indice = 0
        for meuItemSopaCogumelo in self.__sopaCogumelo:
            print(f"\nItem {indice+1}:")
            meuItemSopaCogumelo.mostrar()
            indice += 1
    
    def usarSopaCogumelo(self, parNomeItem):
        indice = 0
        for item in self.__sopaCogumelo:
            nomeDoItem = item.obterNome()
            if nomeDoItem == parNomeItem:
                self.__sopaCogumelo.pop(indice)
                break
            indice += 1
        
    def descartarSopaCogumelos(self):
        self.__comida.pop(3)
        self.__sopaCogumelo.pop(0)

    def quantidadeSopaCogumelos(self):
        quantidade_sopaCogumelos = len(self.__sopaCogumelo)
        return quantidade_sopaCogumelos
    


