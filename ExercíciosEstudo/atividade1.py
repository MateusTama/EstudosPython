class Triangulo:
    def __init__(self, ladoA=0, ladoB=0, ladoC=0):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        conteudo = print(perimetro)
        return conteudo
    
    def getMaiorLado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            maiorLado = print(f"O maior lado é o A, que apresenta {self.ladoA}cm")
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            maiorLado = print(f"O maior lado é o B, que apresenta {self.ladoB}cm")
        elif self.ladoC > self.ladoA and self.ladoC > self.ladoB:
            maiorLado = print(f"O maior lado é o C, que apresenta {self.ladoC}cm")
        elif self.ladoA == self.ladoB and self.ladoB == self.ladoC:
            maiorLado = print(f"Todos os lados são iguais, portante é um triângulo equilátero")
        else:
            maiorLado = print("Dois lados são iguais, portanto é um triângulo isósceles")
        return maiorLado
    
triangulo1 = Triangulo(0,0,0)
triangulo1.calcularPerimetro()
triangulo1.getMaiorLado()
