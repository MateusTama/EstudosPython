#Aula dia 16/08/22 terça feira, programação orientada à objeto.
#Classe modelo de como será o estudante por exemplo, oque o estudante deverá ter, depois disso você cria o objeto tendo oque o modelo indica que ele deveria ter.

#nomeEstudante = ""
#matriculaEstudante = ""
#nascimentoEstudante = ""
#nomeProfessor = ""
#areaProfessor = ""
#cargaHorariaProfessor = ""
#nomeDisciplina = ""
#nomeCurso = ""
#nomeTurma = ""
#anoTurma = ""
#notaEstudante = ""
#frequenciaEstudante = ""

#def matriculaEstudante():
 #   print("Estudante matriculado(a)")
#def calcularMedia():
 #   print("Média Calculada")
#def criarTurma():
 #   print("Turma criada")
#def criarDisciplina():
 #   print("Disciplina criada")

#Classes começam com letras maiúsculas, class ... :

class Estudante:
#Aqui você irá construir o estudante, oque ele deve ter, ser, fazer, etc.
#Variável dentro da classe principal.
# Criar uma função específica que cria todas as variáveis do objeto de classe nesse caso estudante, a função é: "def __init__(self):", self é um recurso que faz a conexão do que acontece dentro das funções e a classe.
# Quando for criar a variável coloque o self primeiro por exemplo: " self.nome ="" " 
    def __init__(self, parNome):
        self.__nome = ""
        self.__matricula = 0 
        self.__nascimento = ""

    def alterarNome(self, parNome):
        self.__nome = parNome

    def mostrarNome(self):
        return self.__nome

    def atestarFrequencia(self):
        print("Estudante: {self.__nome}, frequentando normalmente.")
    def verificarSituacaoNotas(self):
        print("Estudante: {self.__nome}, em recuperação.")
#exemplo de como criariámos o estudante dentro da class.
#classe não executa, não faz nada sozinha, somente serve de modelo para o programa principal.
# __ serve para dizer para o python que essa variável só pode funcionar dentro da classe.
