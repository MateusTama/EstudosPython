class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentualDeAumento):
        self.porcentualDeAumento = porcentualDeAumento / 100
        self.salario += (self.salario * self.porcentualDeAumento)
        conteudo = print(f"Novo salário: {self.salario}")
        return conteudo
    
funcionario1 = Funcionario("Antônio", 1000)
funcionario1.aumentarSalario(10)
