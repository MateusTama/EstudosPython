class Livro:
    def __init__(self, nome, quantidadePaginas, autor, preco):
        self.nome = nome
        self.quantidadePaginas = quantidadePaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        conteudo = print(f"Preço: {self.preco}")
        return conteudo
    
    def setPreco(self, novoPreco):
        self.preco = novoPreco
        conteudo = print(f"Novo Preço: {self.preco}")
        return conteudo
    
livro1 = Livro("O Machete", 210, "Machado de Assís", 35)
livro1.getPreco()
livro1.setPreco(45)