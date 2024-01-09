class Aluno:
    def __init__(self, nome, curso, horasSemDormir):
        self.nome = nome
        self.curso = curso
        self.horasSemDormir = horasSemDormir

    def estudar(self, horasEstudadas):
        self.horasSemDormir += horasEstudadas

    def dormir(self, horasDeSono):
        self.horasSemDormir -= horasDeSono

    def tempoSemDormir(self):
        devendoHoras = self.horasSemDormir * -1
        if self.horasSemDormir < 0:
            conteudo = print(f"Você dormiu demais e está devendo: {devendoHoras} horas de estudo!")
        else:
            conteudo = print(f"Você precisa dormir mais, e possui um saldo de: {self.horasSemDormir} horas para dormir!")
        return conteudo

aluno1 = Aluno("Roberto", "Programação", 8)
aluno1.estudar(10)
aluno1.dormir(2)
aluno1.tempoSemDormir()
