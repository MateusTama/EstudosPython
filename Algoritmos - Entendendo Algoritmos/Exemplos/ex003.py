# Código Lixo - Reformular


# Recursão
# Utilizado por muitos algoritmos

# Função que se reutiliza
# Loops x recursão (programa x programadador)

# Sem recursão com utilização de loops

# def procura_pela_chave(caixa_principal):
#     pilha = main_box.crie_uma_pilha_para_busca()
#     while pilha:
#         caixa = pilha.pegue_uma_caixa()
#         for item in caixa:
#             if item.e_uma_caixa():
#                 pilha.append(item)
#             elif item.e_uma_chave():
#                 print("Achei a chave!")

class Caixa:
    def __init__(self):
        self.itens = []
        self.chave = False

    def adicionarItem(self, item):
        self.itens.append(item)

class Chave:
    def __init__(self):
        self.chave = True

chave = Chave()
caixa = Caixa()
caixa1 = Caixa()
caixa2 = Caixa()
caixa3 = Caixa()
caixa4 = Caixa()
caixa5 = Caixa()

caixa.adicionarItem(caixa1)
caixa1.adicionarItem(caixa2)
caixa2.adicionarItem(caixa3)
caixa3.adicionarItem(caixa4)
caixa4.adicionarItem(caixa5)
caixa5.adicionarItem(chave)

def procura_pela_chave(caixa):
    for item in caixa.itens:
        if item.chave == False:
            print("É uma caixa")
            procura_pela_chave(item)

        if item.chave == True:
            print("É uma chave")
            break

print(procura_pela_chave(caixa))