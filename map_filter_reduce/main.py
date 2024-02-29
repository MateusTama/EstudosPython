# Código com base no vídeo: https://www.youtube.com/watch?v=b1dGlTgFSI0&t=28s
from pprint import pprint
# Importando o reduce
from functools import reduce

produtos = [{'nome':'produto1', 'preco':25.00, 'peso':1.250, 'variacoes':['a','b']},
            {'nome':'produto2', 'preco':20.00, 'peso':3.000, 'variacoes':['c','d']},
            {'nome':'produto3', 'preco':15.00, 'peso':0.900, 'variacoes':['m','n']},
            {'nome':'produto4', 'preco':50.00, 'peso':4.700, 'variacoes':['j','k']},
            ]

# pprint(produtos)

# Pegar apenas 1 campo (list comprehension ou função map)

# Iterador para performance (não salva em memória)

# Usando o map
# Utilizando lambda (funções anônimas)
precos = map(lambda p: p['preco'], produtos)
# Consumimos o primeiro valor
print(next(precos))

print('O for está começando: ')

# Consumindo o restante dos valores
for preco in precos:
    print(preco)

# Iterador consumiu todos os valores (StopIteration)

# print(next(precos))

# Tranformando em lista (Salva em memória)
precos = list(map(lambda p: p['preco'], produtos))
print(precos)

# Exemplo: Aumentando o preço de todos os objetos em 5%
# Round = arredendor casas decimais

precos = list(map(lambda p: round(p['preco'] * 1.05), produtos))
print(precos)

# Fazendo alterações diretamente no dicionário
# **p = unpacking de p, ou seja, retirando todas as chaves que ele possui (p = dict)

precos = list(map(lambda p: {**p ,'preco': round(p['preco'] * 2)}, produtos))
pprint(precos)

precos[0]['variacoes'][0] = 'z'
pprint(precos[0])

# Alterações em "precos" provocam alterações na lista original
pprint(produtos)

# Pegando apenas 1 campo sem utilizar list comprehension ou função map

# Usando List Comprehension

produtos_map = list(map(lambda p: p['preco'], produtos))
print(produtos_map)
produtos_map_list_comprehension = [produto for produto in produtos]
produtos_map_list_comprehension = [produto['preco'] for produto in produtos]
pprint(produtos_map_list_comprehension)

# Usando filter
# Filtrar os objetos

# Filtra os produtos/objetos a partir do retorno de True
produtos_filter = list(filter(lambda p: True, produtos))
pprint(produtos_filter)


# Filtrando por valor
print("Filtrando por valor:")
produtos_filter = list(filter(lambda p: p['preco'] > 20, produtos))
pprint(produtos_filter)

# Combinando map e filter

produtos_map_filter = list(
    # filter se torna o iteravel e o 1 lambda a func
    map(
        lambda p: p['preco'],   
        filter(lambda p: p['preco'] > 20, produtos)
    )
)

print(produtos_map_filter)

# Produtos filter com List Comprehension

print('Produtos filtrados com list comprehension')
# produto (maninpulável) for produto in produtos (for padrão) if
produtos_filter_list_comprehension = [produto['preco'] for produto in produtos if produto['preco'] > 20]
pprint(produtos_filter_list_comprehension)

# precos = []
# for produto in produtos:
#     precos.append(produto['preco'])

# print(precos)

# REDUCE

# Pegar um objeto grande e reduzir em um menor

def preco_reducer(acumulador, produto_atual):
    return acumulador + produto_atual['preco']

print("Somando o preço de todos os objetos com reduce:")
# preco_total = reduce(preco_reducer, produtos, 0)
preco_total = reduce(lambda acumulador, produto_atual: acumulador + produto_atual['preco'], produtos, 0)
print(preco_total)

# REDUCE COM LIST COMPREHENSION

print("Reduce List Comprehension:")

preco_total_list_comprehension = sum([produto['preco'] for produto in produtos])
print(preco_total_list_comprehension)