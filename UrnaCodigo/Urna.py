import urna_funcoes

infoCandidato = "infoCand.txt"
registroVotacao = "regVotacao.txt"

while True:
    menu = urna_funcoes.urnaMenu()
    if menu == 1:
        urna_funcoes.UrnaCadastro(infoCandidato)

    elif menu == 2:
        urna_funcoes.ListarCandidato(infoCandidato)

    elif menu == 3:     
        urna_funcoes.AlterarCandidato(infoCandidato)

    elif menu == 4:
        urna_funcoes.RemoverCandidato(infoCandidato)

    elif menu == 5:
        urna_funcoes.IniciarVotacao(infoCandidato , registroVotacao)

    elif menu == 0:
        print()
        print("Saindo...")
        break

print()
print("Fim do programa!")

