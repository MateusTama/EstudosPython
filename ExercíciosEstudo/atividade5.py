class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def adicionarGasolina(self, quantidadeLitros):
        self.combustivel += quantidadeLitros

    def obterGasolina(self):
        conteudo = print(f"Gasolina: {round(self.combustivel, 3)} litros")
        return conteudo
    
    def dirigir(self, distancia):
        distanciaMaxima = (self.combustivel * self.consumo)
        if distancia <= distanciaMaxima:
            self.combustivel -= (distancia / self.consumo)
        else:
            print(f"Com essa quantidade de gasolina você consegue andar no máximo {distanciaMaxima}km. A viagem não é permitida.")
    
carro1 = Carro(10)
carro1.adicionarGasolina(20)
carro1.obterGasolina()
carro1.dirigir(191)
carro1.obterGasolina()
