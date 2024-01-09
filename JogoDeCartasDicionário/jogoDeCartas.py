import random
#Desenvolvedor: Mateus.
#Colaborades: Ricci, Abraaoso.
#Analista de código: Abraaoso.
#Apoio moral: Leandro, Taynan, Rico. 

baralho = {
    "Ás de copas": 1,
    "2 de copas": 2,
    "3 de copas": 3,
    "4 de copas": 4,
    "5 de copas": 5,
    "6 de copas": 6,
    "7 de copas": 7,
    "8 de copas": 8,
    "9 de copas": 9,
    "10 de copas": 10,
    "Valete de copas": 11,
    "Dama de copas": 12,
    "Rei de copas": 13,
    "Ás de ouro": 1,
    "2 de ouro": 2,
    "3 de ouro": 3,
    "4 de ouro": 4,
    "5 de ouro": 5,
    "6 de ouro": 6,
    "7 de ouro": 7,
    "8 de ouro": 8,
    "9 de ouro": 9,
    "10 de ouro": 10,
    "Valete de ouro": 11,
    "Dama de ouro": 12,
    "Rei de ouro": 13,
    "Ás de espada": 1,
    "2 de espada": 2,
    "3 de espada": 3,
    "4 de espada": 4,
    "5 de espada": 5,
    "6 de espada": 6,
    "7 de espada": 7,
    "8 de espada": 8,
    "9 de espada": 9,
    "10 de espada": 10,
    "Valete de espada": 11,
    "Dama de espada": 12,
    "Rei de espada": 13,
    "Ás de paus": 1,
    "2 de paus": 2,
    "3 de paus": 3,
    "4 de paus": 4,
    "5 de paus": 5,
    "6 de paus": 6,
    "7 de paus": 7,
    "8 de paus": 8,
    "9 de paus": 9,
    "10 de paus": 10,
    "Valete de paus": 11,
    "Dama de paus": 12,
    "Rei de paus": 13,

}

jogadas = int(input("Com quantas cartas você deseja jogar? 1-26: "))
pontosComputador = 0

for cartasComputador in range(jogadas):
    listaDeCartas = list(baralho.keys())
    cartaEscolhida = random.choice(listaDeCartas)
    print("Cartas escolhidas para o Computador:",cartaEscolhida)
    print()
    pontosComputador += baralho[cartaEscolhida]
    del baralho[cartaEscolhida]
    #print(baralho)

input("As cartas do computador foram escolhidas... Pressione ENTER para continuar.")
print()
pontosJogador = 0

for cartasJogador in range(jogadas):
    listaDeCartas = list(baralho.keys())
    cartaEscolhida = random.choice(listaDeCartas)
    print("Cartas escolhidas para o Jogador:",cartaEscolhida)
    print()
    pontosJogador += baralho[cartaEscolhida]
    del baralho[cartaEscolhida]
    #print(baralho)

input("As cartas do jogador foram escolhidas... Pressione ENTER para continuar.")
print()
print("RESULTADO:")
print()

if pontosComputador > pontosJogador:
    print("Vitória do computador")
    print()
    print(f"Pontos do computador: {pontosComputador}\nPontos do jogador: {pontosJogador}")

elif pontosJogador > pontosComputador:
    print("Vitória do jogador")
    print()
    print(f"Pontos do jogador: {pontosJogador}\nPontos do compuatador: {pontosComputador}")

else: 
    print("EMPATE!")
    print()
    print("O compuatador e o jogador empataram!!")
    print()
    print(f"Pontos do computador: {pontosComputador}\nPontos do jogador: {pontosJogador}")
    print()




    

