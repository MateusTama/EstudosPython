#Crie uma classe Estudante que tenha os seguintes atributos: nome e turma.
#• Crie uma classe Professor que tenha os seguintes atributos: nome e disciplina.
#• Crie uma classe Clube que tenha os seguintes atributos: nome, professorResponsavel,
#horarioReuniao e uma lista de membros.


#Quando for criar um objeto da classe Clube, lembre-se que o atributo
#professorResponsável deve ser um objeto da classe Professor.
#o A lista de membros deve começar vazia.
#o Crie o método adicionarMembro que recebe um objeto do tipo Estudante como
#parâmetro e o adiciona na lista de membros.


class Estudante:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma

class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

class Clube: 
    def __init__(self, nome, professorResponsavel, horarioReuniao):
        self.nome = nome
        self.professorResponsavel = professorResponsavel
        self.horarioReuniao = horarioReuniao
        self.membros = []
    
    def adicionarMembro(self, parEstudante):
        self.membros.append(parEstudante)
    