# Criar um dicionário vazio:
dicionario = {}

# Criar um dicionário com itens:
dicionario = {  "nome" : "abc",
                "email" : "x@y.z",
                "telefone" : 12345 }

# Mostrar o valor de um item do dicionário:
print(dicionario["nome"])
# Isso vai dar erro:
# print(dicionario[2])

# Procurando chaves com in 
busca = input("Informe o termo para buscar no dicionário: ")
if busca in dicionario:
    print(f"Termo encontrado. chave: {busca} / valor: {dicionario[busca]}")
else:
    print("Termo não encontrado.")

# Adicionar elementos no dicionário
# Se a chave já existir, sobrescreve
# Se a chave não existir, cria novo
dicionario["endereco"] = "Rua blablabla"

# Deletar um Elemento do dicionário
del(dicionario["endereco"])
# itemRemovido = dicionario.pop("endereco")
# print(itemRemovido)

# Descobrir o número de elementos do dicionário
quantosItens = len(dicionario)
print(f"No momento o dicionário possui {quantosItens} itens.")

# Usar for para percorrer o dicionário
for chaves in dicionario:
    print(f"chave do item: {chaves} / valor do item: {dicionario[chaves]}")

chaves = dicionario.keys()
valores = dicionario.values()