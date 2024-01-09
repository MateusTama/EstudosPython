class Produto:
    def __init__(self, parCodigo, parFabricante, parNome, parPreco):
        self.__codigo = parCodigo
        self.__fabricante = parFabricante
        self.__nome = parNome
        self.__preco = parPreco

    # Código
    def alterarCodigo(self, parCodigo):
        self.__codigo = parCodigo

    def obterCodigo(self):
        return self.__codigo

    # Fabricante
    def alterarFabricante(self, parFabricante):
        self.__fabricante = parFabricante

    def obterFabricante(self):
        return self.__fabricante 

    # Nome   
    def alterarNome(self, parNome):
        self.__nome = parNome

    def obterNome(self):
        return self.__nome 

    # Preco
    def alterarPreco(self, parPreco):
        self.__preco = parPreco

    def obterPreco(self):
        return float(self.__preco)
         
