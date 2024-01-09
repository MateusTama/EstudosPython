class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Equipe:
    def __init__(self, projeto):
        self.projeto = projeto
        self.participantes = []

    def adicionarParticipantes(self, parAluno):
        #VERIFICAÇÃO DE ALUNOS DUPLICADOS VIA CPF
        contadorAlunos = 0
        listaAlunoDuplicado = []
        for participantesProjeto in self.participantes:
            if parAluno.cpf not in participantesProjeto.cpf:
                contadorAlunos += 1
            else:
                listaAlunoDuplicado.append(parAluno.nome)
        if contadorAlunos == len(self.participantes):
            self.participantes.append(parAluno)
        else:
            print(f"O aluno presente na lista: {listaAlunoDuplicado} já está na lista de participantes deste projeto!")

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []
    
    def mostrarEquipes(self):
        #FUNÇÃO MOSTRAR TODAS AS EQUIPES
        indice = 0
        indiceMembro = 0
        for equipe in self.equipes:
            print()
            indice += 1
            indiceMembro = 0
            print(f"Equipe {indice}: {equipe.projeto}")
            for membros in equipe.participantes:
                indiceMembro += 1
                print(f"Participante {indiceMembro}: {membros.nome}")

    def criarEquipe(self, equipeAdicionar):
        # if len(self.equipes) > 0:
        #     for equipe in self.equipes:
        #         if equipeAdicionar.projeto == equipe.projeto:
        #             for membros in equipeAdicionar.participantes:
        #                 for membrosAdicionar in equipe.participantes:
        #                     if membros.cpf == membrosAdicionar.cpf:
        #                         print(f"Erro: O aluno {membros.nome} já está em um outro projeto de {equipe.projeto}!")
        #                         print("O aluno será removido do projeto ")
        #                         equipeAdicionar.participantes.remove(membrosAdicionar)
        #         else:
        #             conteudo = print("Adicionando equipe")
        #             self.equipes.append(equipeAdicionar)
        #             return conteudo
        # else:
        #     self.equipes.append(equipeAdicionar)
        
        #Testa se já possui uma equipe na lista de Equipes, se não tiver adiciona automaticamente
        if len(self.equipes) > 0:
            contadorMesmoProjeto = 0
            equipesIguais = []
            for equipe in self.equipes:
                if equipeAdicionar.projeto == equipe.projeto:
                    equipesIguais.append(equipe)
                    contadorMesmoProjeto += 1
                elif equipeAdicionar.projeto != equipe.projeto:
                    pass
                else:
                    print("Erro. Verifique os valores.")
            contadorAlunosIguais = 0
            alunosIguais = []
            if contadorMesmoProjeto >= 1:
                for equipe_igual in equipesIguais:
                    for membros in equipe_igual.participantes:
                        for membrosAdicionar in equipeAdicionar.participantes:
                            if membros.cpf == membrosAdicionar.cpf:
                                contadorAlunosIguais += 1
                                alunosIguais.append(membrosAdicionar.nome)
                            elif membros.cpf != membros.cpf:
                                pass
            else: 
                pass
            if contadorAlunosIguais >= 1:
                print(f"O projeto '{equipeAdicionar.projeto}' não pode ser criado. Pois os alunos presentes na lista: {alunosIguais} já participam de outro projeto.")
            elif contadorAlunosIguais == 0 and contadorMesmoProjeto == 0:
                self.equipes.append(equipeAdicionar)
            elif contadorAlunosIguais == 0 and contadorMesmoProjeto >= 1:
                self.equipes.append(equipeAdicionar)
        else:
            self.equipes.append(equipeAdicionar)

            
aluno1 = Aluno("Mateus", "12345678900")
aluno2 = Aluno("Monstro", "45678912300")
aluno3 = Aluno("Iago", "99988877700")

equipe1 = Equipe("Programação")
equipe1.adicionarParticipantes(aluno1)
equipe1.adicionarParticipantes(aluno2)

equipe2 = Equipe("Matemática")
equipe2.adicionarParticipantes(aluno3)

equipe3 = Equipe("Programação")
equipe3.adicionarParticipantes(aluno3)
equipe3.adicionarParticipantes(aluno3)

adicionarEquipes = GerenciadorEquipes()
adicionarEquipes.criarEquipe(equipe1)
adicionarEquipes.criarEquipe(equipe2)
adicionarEquipes.criarEquipe(equipe3)

adicionarEquipes.mostrarEquipes()
