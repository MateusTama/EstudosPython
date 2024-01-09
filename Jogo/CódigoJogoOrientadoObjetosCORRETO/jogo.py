#Trabalho feito por Mateus Tamasia, Eduardo Kohler e Lucas da Silva Valim

import random
import classesJogo

nomePlayer = input("Bem vindo jogador, informe seu nick: ")
print()
categoriaPlayer = input("Informe sua categoria: ")
jogador = classesJogo.Player(nomePlayer, categoriaPlayer)

nomePlayer = jogador.obterNome()
categoriaPlayer = jogador.obterCategoria()

#O jogo começa com o jogador chegando em uma loja para receber seus primeiros itens. Simule o diálogo entre o jogador e o vendedor. Nesse momento o vendedor vai dar 5 itens de graça para o jogador poder começar o jogo. Invente os itens, crie os objetos da classe Item e os adicione ao inventário do jogador.

print()
print(f"Vendedor -- Bem vindo a Monster Shop, o que você deseja {nomePlayer}?")

input()

print(f"{nomePlayer} -- Olá, eu estou a procura itens para minha aventura.")

input()

print(f"Vendedor -- Pegue 5 itens para começar sua aventura!")

input()

print(f"{nomePlayer} -- Obrigado.")

#vida das frutas
vidaRecuperada1 = random.randint(1,20)

novoItem1 = classesJogo.Item("Arco","Arma que atira flechas",0,1) 
jogador.inventario.adicionarItem(novoItem1)

novoItem2 = classesJogo.Item("Maça","Comida que aumenta a vida",vidaRecuperada1,1)
jogador.inventario.adicionarItem(novoItem2)
jogador.inventario.adicionarItemComida(novoItem2)
jogador.inventario.adicionarItemMaca(novoItem2)

vidaRecuperada2 = random.randint(1,20)

novoItem3 = classesJogo.Item("Poção","Concebe cura",vidaRecuperada2,1)
jogador.inventario.adicionarItem(novoItem3)
jogador.inventario.adicionarItemComida(novoItem3)
jogador.inventario.adicionarItemPocao(novoItem3)

novoItem4 = classesJogo.Item("Espada","Serve para atacar os inimigos",0,1)
jogador.inventario.adicionarItem(novoItem4)

novoItem5 = classesJogo.Item("Escudo","Serve para proteger a si mesmo",0,1)
jogador.inventario.adicionarItem(novoItem5)

jogador.inventario.mostrarInventario()

#PRIMEIRO MONSTRO

print()
print(f"Essa é sua primeira batalha {nomePlayer}. Divirta-se!")
print()

input("Pressione ENTER para derrotá-lo...")

#DANO RECEBIDO PELO PRIMEIRO MONSTRO

vidaPerdida1 = random.randint(1,20) 
jogador.alterarVida(vidaPerdida1 * -1)

print()
print(f"Parabéns! Você derrotou o monstro, porém perdeu {vidaPerdida1} pontos de vida.")
print()
print("Pela sua vitória vamos lhe dar um bife e um diamante.")

vidaRecuperada3 = random.randint(1,20)

novoItem6 = classesJogo.Item("Bife","Alimento que aumenta seus pontos de vida",vidaRecuperada3,1) 
jogador.inventario.adicionarItem(novoItem6)
jogador.inventario.adicionarItemComida(novoItem6)
jogador.inventario.adicionarItemBife(novoItem6)

novoItem7 = classesJogo.Item("Diamante","Jóia de beleza indescritível",0,1)
jogador.inventario.adicionarItem(novoItem7)

#SEGUNDO MONSTRO

print()
print("Um novo monstro apareceu viajante! Derrote-o.")
print()

input("Esse monstro é muito forte, você sofreu um golpe. Pressione ENTER para contra-atacar...")

#DANO RECEBIDO PELO SEGUNDO MONSTRO

vidaPerdida2 = random.randint(1,20)
jogador.alterarVida(vidaPerdida2 * -1)

print()
print(f"Parabéns! Você conseguiu derrotar o monstro, porém aquele golpe lhe fez perder {vidaPerdida2} pontos de vida.")
print()
input("Pressione ENTER para vasculhar o monstro...")
print()
print("Com o monstro foram encontrados os seguintes itens: uma comida e uma chave!")

vidaRecuperada4 = random.randint(1,20)

novoItem8 = classesJogo.Item("Sopa de Cogumelos","Alimento que aumenta seus pontos de vida",vidaRecuperada4,1)   
jogador.inventario.adicionarItem(novoItem8)
jogador.inventario.adicionarItemComida(novoItem8)
jogador.inventario.adicionarItemSopaCogumelo(novoItem8)

novoItem9 = classesJogo.Item("Chave","Utensílio de utilidade desconhecida",0,1)
jogador.inventario.adicionarItem(novoItem9)

#CHEGAR AO CASTELO

print()
input("Pressione ENTER para continuar pelo trajeto indicado...")
print()
print(f"{nomePlayer} -- O que é aquela residência ao topo da colina?")
print()
print("Você acabou de chegar num castelo!")
print()
print(f"{nomePlayer} -- Que estranho, para entrar neste castelo é necessário uma chave.")
print()
print(f"{nomePlayer} -- Lembro de ter ganhado uma quando matei aquele monstro. Vou testá-la...")
print()
input("A PORTA SE MEXE! Pressione ENTER para entrar...")

#USAR A CHAVE

jogador.inventario.usarChave()

#ACHAR ANEL E AMULETO

print()
print("Você entra no castelo...")
print()
input("Você começa a explorar todos os arredores do novo ambiente. Até que... Pressione ENTER para continuar...")
print()
print("Você encontrou um anel e um amuleto! Guarde-os bem, eles podem ser muito importantes.")

novoItem10 = classesJogo.Item("Anel","Utensílio para melhorar sua proteção",25,1)
jogador.inventario.adicionarItem(novoItem10)
jogador.inventario.adicionarItemProtecao(novoItem10)

novoItem11 = classesJogo.Item("Amuleto","Utensílio que melhora a proteção",25,1)
jogador.inventario.adicionarItem(novoItem11)
jogador.inventario.adicionarItemProtecao(novoItem11)

#CHEGAR A CAVERNA

print()
print("Você segue adiante...")
print()
print("Parabéns! Você chegou na Caverna dos Horrores. Agora é TUDO ou NADA!")
print()
input("Pressione ENTER para começar o desafio...")

#INICIAR DESAFIO

print("Guardião da Caverna -- Bem vindo viajante! já que você chegou até aqui, lhe proponho um desafio bem simples. Você está vendo essa moeda aqui? Ela vai decidir o seu destino.")
print()

resultado = random.randint(1,2)
print(resultado)
decisao = int(input("Cara ou coroa:\n\n1- Cara\n2- Coroa\n\nFaça sua escolha: "))
print()


if(decisao == resultado):
    print("Parabéns viajante, você finalizou o desafio. Irei lhe dar 2 recompensas para continuar sua jornada: uma Barra de Nutrientes e um Livro de Mágias!")
    print()

    vidaRecuperada5 = random.randint(1,20)

    novoItem12 = classesJogo.Item("Barra de Nutrientes","Alimento nutritivo que vai melhorar sua vida",vidaRecuperada5,1)
    jogador.inventario.adicionarItem(novoItem12)
    jogador.inventario.adicionarItemComida(novoItem12)
    jogador.inventario.adicionarItemBarrinha(novoItem12)

    novoItem13 = classesJogo.Item("Livro de Mágias","Série de feitiços para enfraquecer seus oponentes",0,1)
    jogador.inventario.adicionarItem(novoItem13)
    print()
    adicionar = input("Deseja adicionar o Livro de Mágias? s/n: ")
    if(adicionar == "s"):
        indice = jogador.inventario.descartarItem()
        jogador.inventario.adicionarItem(novoItem13)
        if indice == 10:
            jogador.inventario.descartarBarrinha()
        elif indice == 9:
            jogador.inventario.descartarAmuleto()
        elif indice == 8:
            jogador.inventario.descartarAnel()
        elif indice == 1:
            jogador.inventario.descartarMaca()
        elif indice == 2:
            jogador.inventario.descartarPocao()
        elif indice == 5:
            jogador.inventario.descartarBife()
        elif indice == 7:
            jogador.inventario.descartarSopaCogumelos()

elif(decisao != resultado and decisao == 2 or decisao == 1):
    print("Parece que você não escolheu muito bem o seu destino...")
    print()
    print("Como consequência você acaba de perder metade dos seus pontos de vida")
    vida = jogador.obterVida()
    vidaPerdida3 = (vida * 0.5) * -1
    jogador.alterarVida(vidaPerdida3)
    print()
    print(f"Você ainda tem {jogador.obterVida()} pontos de vida!")

else:
    print("Valor inválido.")

#ÚLTIMO MONSTRO

print()
input("Pressione ENTER para continuar sua jornada...")
print()
print("Você finalmente chegou ao último monstro! Derrote-o e sua aventura acabará.")
print()
print("Aproveite este momento para pegá-lo desprevinido.")
print()
input("Pressione ENTER para atacá-lo...")

#ENCONTRA O MONSTRO

#PRIMEIRA BATALHA

#DANO RECEBIDO PELO PRIMEIRO ATAQUE

vida1 = jogador.obterVida()
print(vida1)
while(vida1 > 0):

    vidaPerdida4 = random.randint(1,20) 
    jogador.alterarVida(vidaPerdida4 * -1)

    print()
    print(f"Muito Bem {nomePlayer}! Você realizou seu primeiro ataque, porém o monstro revidou e você perdeu {vidaPerdida4} pontos de vida.")
    print()
    vida1 = jogador.obterVida()

    #USAR COMIDA

    quantidade_maca = jogador.inventario.quantidadeMaca()
    quantidade_pocao = jogador.inventario.quantidadePocao()
    quantidade_bife = jogador.inventario.quantidadeBife()
    quantidade_sopaCogumelos = jogador.inventario.quantidadeSopaCogumelos()
    quantidade_barrinha = jogador.inventario.quantidadeBarrinha()
    quantidade_protecao = jogador.inventario.quantidadeProtecao()
    quantidade_comida = jogador.inventario.quantidadeComida()
    if(vida1 == 0 and quantidade_comida > 0):
        vidaRecuperadaTotal = 0
        if(quantidade_maca > 0):
            maca = jogador.inventario.usarItem("Maça")
            jogador.inventario.usarComida("Maça")
            jogador.inventario.usarMaca("Maça")  
            jogador.alterarVida(maca)
            vidaRecuperadaTotal += maca
        if(quantidade_pocao > 0):
            pocao = jogador.inventario.usarItem("Poção")
            jogador.inventario.usarComida("Poção")
            jogador.inventario.usarPocao("Poção")
            jogador.alterarVida(pocao)
            vidaRecuperadaTotal += pocao
        if(quantidade_bife > 0):
            bife = jogador.inventario.usarItem("Bife")
            jogador.inventario.usarComida("Bife")
            jogador.inventario.usarBife("Bife")
            jogador.alterarVida(bife)
            vidaRecuperadaTotal += bife
        if(quantidade_sopaCogumelos > 0):
            sopaCogumelo = jogador.inventario.usarItem("Sopa de Cogumelos")
            jogador.inventario.usarComida("Sopa de Cogumelos")
            jogador.inventario.usarSopaCogumelo("Sopa de Cogumelos")
            jogador.alterarVida(sopaCogumelo)
            vidaRecuperadaTotal += sopaCogumelo
        if(decisao == resultado and quantidade_barrinha > 0):
            barraDeNutrientes = jogador.inventario.usarItem("Barra de Nutrientes")
            jogador.inventario.usarComida("Barra de Nutrientes")
            jogador.inventario.usarBarrinha("Barra de Nutrientes")            
            jogador.alterarVida(barraDeNutrientes)
            vidaRecuperadaTotal += barraDeNutrientes
        print()
        print("Sua vida chegou a 0.")
        print()
        print(f"Todas as comidas foram usadas! Um total de {vidaRecuperadaTotal} pontos de vida foram regenerados.")
        print()

    elif(vida1 == 0 and quantidade_protecao > 1):
        amuleto = jogador.inventario.usarItem("Amuleto")
        jogador.inventario.usarProtecao("Amuleto")
        jogador.alterarVida(amuleto)
        anel = jogador.inventario.usarItem("Anel")
        jogador.inventario.usarProtecao("Anel")
        jogador.alterarVida(anel)
        print()
        print("Sua vida chegou a 0, porém você tinha os itens de proteção!")
        print()

    elif(vida1 == 0):
        print()
        print("Você morreu!")
        print()
        break
        
    #SEGUNDA BATALHA

    #DANO RECEBIDO PELO SEGUNDO ATAQUE

    vidaPerdida5 = random.randint(1,20) 
    jogador.alterarVida(vidaPerdida5 * -1)

    print("O monstro ainda não morreu, ele aparenta ser mais forte que os outros. Continue atacando ele para matá-lo!")
    print()
    input("Pressione ENTER para atacá-lo...")
    print()
    print("Seu ataque foi muito efetivo!")
    print()
    print(f"O monstro lhe acertou e tirou {vidaPerdida5} pontos de vida.")
    vida1 = jogador.obterVida()
    print()

    #USAR COMIDA

    quantidade_maca = jogador.inventario.quantidadeMaca()
    quantidade_pocao = jogador.inventario.quantidadePocao()
    quantidade_bife = jogador.inventario.quantidadeBife()
    quantidade_sopaCogumelos = jogador.inventario.quantidadeSopaCogumelos()
    quantidade_barrinha = jogador.inventario.quantidadeBarrinha()
    quantidade_protecao = jogador.inventario.quantidadeProtecao()
    quantidade_comida = jogador.inventario.quantidadeComida()
    if(vida1 == 0 and quantidade_comida > 0):
        vidaRecuperadaTotal = 0
        if(quantidade_maca > 0):
            maca = jogador.inventario.usarItem("Maça")
            jogador.inventario.usarComida("Maça")
            jogador.inventario.usarMaca("Maça")  
            jogador.alterarVida(maca)
            vidaRecuperadaTotal += maca
        if(quantidade_pocao > 0):
            pocao = jogador.inventario.usarItem("Poção")
            jogador.inventario.usarComida("Poção")
            jogador.inventario.usarPocao("Poção")
            jogador.alterarVida(pocao)
            vidaRecuperadaTotal += pocao
        if(quantidade_bife > 0):
            bife = jogador.inventario.usarItem("Bife")
            jogador.inventario.usarComida("Bife")
            jogador.inventario.usarBife("Bife")
            jogador.alterarVida(bife)
            vidaRecuperadaTotal += bife
        if(quantidade_sopaCogumelos > 0):
            sopaCogumelo = jogador.inventario.usarItem("Sopa de Cogumelos")
            jogador.inventario.usarComida("Sopa de Cogumelos")
            jogador.inventario.usarSopaCogumelo("Sopa de Cogumelos")
            jogador.alterarVida(sopaCogumelo)
            vidaRecuperadaTotal += sopaCogumelo
        if(decisao == resultado and quantidade_barrinha > 0):
            barraDeNutrientes = jogador.inventario.usarItem("Barra de Nutrientes")
            jogador.inventario.usarComida("Barra de Nutrientes")
            jogador.inventario.usarBarrinha("Barra de Nutrientes")            
            jogador.alterarVida(barraDeNutrientes)
            vidaRecuperadaTotal += barraDeNutrientes
        print()
        print("Sua vida chegou a 0.")
        print()
        print(f"Todas as comidas foram usadas! Um total de {vidaRecuperadaTotal} pontos de vida foram regenerados.")
        print()

    elif(vida1 == 0 and quantidade_protecao > 1):
        amuleto = jogador.inventario.usarItem("Amuleto")
        jogador.inventario.usarProtecao("Amuleto")
        jogador.alterarVida(amuleto)
        anel = jogador.inventario.usarItem("Anel")
        jogador.inventario.usarProtecao("Anel")
        jogador.alterarVida(anel)
        print()
        print("Sua vida chegou a 0, porém você tinha os itens de proteção!")
        print()

    elif(vida1 == 0):
        print()
        print("Você morreu!")
        print()
        break

    #TERCEIRA BATALHA

    #DANO RECEBIDO PELO TERCEIRO ATAQUE

    vidaPerdida6 = random.randint(1,20) 
    jogador.alterarVida(vidaPerdida6 * -1)

    print("Esse monstro realmente possui mais vida, provavelmente é o último deles. Ataque novamente!")
    print()
    input("Pressione ENTER para atacá-lo...")
    print()
    print("Você conseguiu retirar causar muito dano!")
    print()
    print(f"Pórem o monstro previu seu ataque e conseguiu lhe arrancar {vidaPerdida6} pontos de vida.")
    print()
    vida1 = jogador.obterVida()

    #USAR COMIDA

    quantidade_maca = jogador.inventario.quantidadeMaca()
    quantidade_pocao = jogador.inventario.quantidadePocao()
    quantidade_bife = jogador.inventario.quantidadeBife()
    quantidade_sopaCogumelos = jogador.inventario.quantidadeSopaCogumelos()
    quantidade_barrinha = jogador.inventario.quantidadeBarrinha()
    quantidade_protecao = jogador.inventario.quantidadeProtecao()
    quantidade_comida = jogador.inventario.quantidadeComida()
    if(vida1 == 0 and quantidade_comida > 0):
        vidaRecuperadaTotal = 0
        if(quantidade_maca > 0):
            maca = jogador.inventario.usarItem("Maça")
            jogador.inventario.usarComida("Maça")
            jogador.inventario.usarMaca("Maça")  
            jogador.alterarVida(maca)
            vidaRecuperadaTotal += maca
        if(quantidade_pocao > 0):
            pocao = jogador.inventario.usarItem("Poção")
            jogador.inventario.usarComida("Poção")
            jogador.inventario.usarPocao("Poção")
            jogador.alterarVida(pocao)
            vidaRecuperadaTotal += pocao
        if(quantidade_bife > 0):
            bife = jogador.inventario.usarItem("Bife")
            jogador.inventario.usarComida("Bife")
            jogador.inventario.usarBife("Bife")
            jogador.alterarVida(bife)
            vidaRecuperadaTotal += bife
        if(quantidade_sopaCogumelos > 0):
            sopaCogumelo = jogador.inventario.usarItem("Sopa de Cogumelos")
            jogador.inventario.usarComida("Sopa de Cogumelos")
            jogador.inventario.usarSopaCogumelo("Sopa de Cogumelos")
            jogador.alterarVida(sopaCogumelo)
            vidaRecuperadaTotal += sopaCogumelo
        if(decisao == resultado and quantidade_barrinha > 0):
            barraDeNutrientes = jogador.inventario.usarItem("Barra de Nutrientes")
            jogador.inventario.usarComida("Barra de Nutrientes")
            jogador.inventario.usarBarrinha("Barra de Nutrientes")            
            jogador.alterarVida(barraDeNutrientes)
            vidaRecuperadaTotal += barraDeNutrientes
        print()
        print("Sua vida chegou a 0.")
        print()
        print(f"Todas as comidas foram usadas! Um total de {vidaRecuperadaTotal} pontos de vida foram regenerados.")
        print()

    elif(vida1 == 0 and quantidade_protecao > 1):
        amuleto = jogador.inventario.usarItem("Amuleto")
        jogador.inventario.usarProtecao("Amuleto")
        jogador.alterarVida(amuleto)
        anel = jogador.inventario.usarItem("Anel")
        jogador.inventario.usarProtecao("Anel")
        jogador.alterarVida(anel)
        print()
        print("Sua vida chegou a 0, porém você tinha os itens de proteção!")
        print()

    elif(vida1 == 0):
        print()
        print("Você morreu!")
        print()
        break

    #QUARTA BATALHA

    #DANO RECEBIDO PELO QUARTO ATAQUE

    vidaPerdida7 = random.randint(1,20) 
    jogador.alterarVida(vidaPerdida7 * -1)

    print("Caramba! O monstro não morre! Ataque ele novamente.")
    print()
    input("Pressione ENTER para atacá-lo...")
    print()
    print("Esse golpe sem dúvidas foi o mais efetivo, parece que você atingiu seu ponto fraco!")
    print()
    print(f"O monstro conseguiu revidar e lhe tirou {vidaPerdida7} pontos de vida.")
    print()
    vida1 = jogador.obterVida()

    #USAR COMIDA

    quantidade_maca = jogador.inventario.quantidadeMaca()
    quantidade_pocao = jogador.inventario.quantidadePocao()
    quantidade_bife = jogador.inventario.quantidadeBife()
    quantidade_sopaCogumelos = jogador.inventario.quantidadeSopaCogumelos()
    quantidade_barrinha = jogador.inventario.quantidadeBarrinha()
    quantidade_protecao = jogador.inventario.quantidadeProtecao()
    quantidade_comida = jogador.inventario.quantidadeComida()
    if(vida1 == 0 and quantidade_comida > 0):
        vidaRecuperadaTotal = 0
        if(quantidade_maca > 0):
            maca = jogador.inventario.usarItem("Maça")
            jogador.inventario.usarComida("Maça")
            jogador.inventario.usarMaca("Maça")  
            jogador.alterarVida(maca)
            vidaRecuperadaTotal += maca
        if(quantidade_pocao > 0):
            pocao = jogador.inventario.usarItem("Poção")
            jogador.inventario.usarComida("Poção")
            jogador.inventario.usarPocao("Poção")
            jogador.alterarVida(pocao)
            vidaRecuperadaTotal += pocao
        if(quantidade_bife > 0):
            bife = jogador.inventario.usarItem("Bife")
            jogador.inventario.usarComida("Bife")
            jogador.inventario.usarBife("Bife")
            jogador.alterarVida(bife)
            vidaRecuperadaTotal += bife
        if(quantidade_sopaCogumelos > 0):
            sopaCogumelo = jogador.inventario.usarItem("Sopa de Cogumelos")
            jogador.inventario.usarComida("Sopa de Cogumelos")
            jogador.inventario.usarSopaCogumelo("Sopa de Cogumelos")
            jogador.alterarVida(sopaCogumelo)
            vidaRecuperadaTotal += sopaCogumelo
        if(decisao == resultado and quantidade_barrinha > 0):
            barraDeNutrientes = jogador.inventario.usarItem("Barra de Nutrientes")
            jogador.inventario.usarComida("Barra de Nutrientes")
            jogador.inventario.usarBarrinha("Barra de Nutrientes")            
            jogador.alterarVida(barraDeNutrientes)
            vidaRecuperadaTotal += barraDeNutrientes
        print()
        print("Sua vida chegou a 0.")
        print()
        print(f"Todas as comidas foram usadas! Um total de {vidaRecuperadaTotal} pontos de vida foram regenerados.")
        print()

    elif(vida1 == 0 and quantidade_protecao > 1):
        amuleto = jogador.inventario.usarItem("Amuleto")
        jogador.inventario.usarProtecao("Amuleto")
        jogador.alterarVida(amuleto)
        anel = jogador.inventario.usarItem("Anel")
        jogador.inventario.usarProtecao("Anel")
        jogador.alterarVida(anel)
        print()
        print("Sua vida chegou a 0, porém você tinha os itens de proteção!")

    elif(vida1 == 0):
        print()
        print("Você morreu!")
        print()
        break

    #QUINTA BATALHA

    #DANO RECEBIDO PELO QUINTO ATAQUE

    vidaPerdida8 = random.randint(1,20) 
    jogador.alterarVida(vidaPerdida8 * -1)

    print("Acredito que este seja o golpe final. Ataque-o viajante, e finalize sua aventura!")
    print()
    input("Pressione ENTER para atacá-lo...")
    print()
    print(f"Mesmo assim, esse monstro é muito forte, e conseguiu lhe acertar um golpe que tirou {vidaPerdida8} pontos de vida")
    print()
    vida1 = jogador.obterVida()

    #USAR COMIDA

    quantidade_maca = jogador.inventario.quantidadeMaca()
    quantidade_pocao = jogador.inventario.quantidadePocao()
    quantidade_bife = jogador.inventario.quantidadeBife()
    quantidade_sopaCogumelos = jogador.inventario.quantidadeSopaCogumelos()
    quantidade_barrinha = jogador.inventario.quantidadeBarrinha()
    quantidade_protecao = jogador.inventario.quantidadeProtecao()
    quantidade_comida = jogador.inventario.quantidadeComida()
    if(vida1 == 0 and quantidade_comida > 0):
        vidaRecuperadaTotal = 0
        if(quantidade_maca > 0):
            maca = jogador.inventario.usarItem("Maça")
            jogador.inventario.usarComida("Maça")
            jogador.inventario.usarMaca("Maça")  
            jogador.alterarVida(maca)
            vidaRecuperadaTotal += maca
        if(quantidade_pocao > 0):
            pocao = jogador.inventario.usarItem("Poção")
            jogador.inventario.usarComida("Poção")
            jogador.inventario.usarPocao("Poção")
            jogador.alterarVida(pocao)
            vidaRecuperadaTotal += pocao
        if(quantidade_bife > 0):
            bife = jogador.inventario.usarItem("Bife")
            jogador.inventario.usarComida("Bife")
            jogador.inventario.usarBife("Bife")
            jogador.alterarVida(bife)
            vidaRecuperadaTotal += bife
        if(quantidade_sopaCogumelos > 0):
            sopaCogumelo = jogador.inventario.usarItem("Sopa de Cogumelos")
            jogador.inventario.usarComida("Sopa de Cogumelos")
            jogador.inventario.usarSopaCogumelo("Sopa de Cogumelos")
            jogador.alterarVida(sopaCogumelo)
            vidaRecuperadaTotal += sopaCogumelo
        if(decisao == resultado and quantidade_barrinha > 0):
            barraDeNutrientes = jogador.inventario.usarItem("Barra de Nutrientes")
            jogador.inventario.usarComida("Barra de Nutrientes")
            jogador.inventario.usarBarrinha("Barra de Nutrientes")            
            jogador.alterarVida(barraDeNutrientes)
            vidaRecuperadaTotal += barraDeNutrientes
        print()
        print("Sua vida chegou a 0.")
        print()
        print(f"Todas as comidas foram usadas! Um total de {vidaRecuperadaTotal} pontos de vida foram regenerados.")
        print()

    elif(vida1 == 0 and quantidade_protecao > 1):
        amuleto = jogador.inventario.usarItem("Amuleto")
        jogador.inventario.usarProtecao("Amuleto")
        jogador.alterarVida(amuleto)
        anel = jogador.inventario.usarItem("Anel")
        jogador.inventario.usarProtecao("Anel")
        jogador.alterarVida(anel)
        print()
        print("Sua vida chegou a 0, porém você tinha os itens de proteção!")
        print()

    elif(vida1 == 0):
        print()
        print("Você morreu!")
        print()
        break

    vida1 = jogador.obterVida()
    jogador.inventario.mostrarInventario()

    #ÚLTIMO GOLPE

    print("Acredito que este seja o golpe final. Ataque-o viajante, e finalize sua aventura!")
    print()
    input("Pressione ENTER para atacá-lo...")
    print()
    print("O monstro morreu!")
    print()
    print(f"Parabéns viajante, você venceu! Ainda restaram-lhe {vida1} pontos de vida.")
    print()
    break

print("Fim de jogo.")
















