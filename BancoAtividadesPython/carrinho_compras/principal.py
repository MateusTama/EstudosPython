import classeProduto

carrinho = []
total = 0

while True:
    # usa o tamanho da lista como código para o produto
    codigo = len(carrinho)+1
    nome = input("Nome: ")
    fabricante = input("Fabricante: ")
    preco = input("Preço: ")
    # cria o objeto 
    produto = classeProduto.Produto(codigo,fabricante,nome,preco)
    # adiciona o objeto na lista 
    carrinho.append(produto)
    # pergunta se quer continuar
    continuar = input("Adicionar mais produtos? ")
    if continuar == "n":
        break

# depois de sair da repetição, soma o preco de todos 
# os produtos do carrinho acessando a função obterPreco de
# cada objeto da lista
for item in carrinho:
    codigo = item.obterCodigo()
    fabricante = item.obterFabricante()
    nome = item.obterNome()
    preco = item.obterPreco()
    print(f"{codigo} {nome} R$ {preco}")
    total += preco

print(f"Total da compra: {total}")
