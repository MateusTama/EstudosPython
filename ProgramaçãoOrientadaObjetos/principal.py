import ClasseEstudante 

#Ele cria uma instância.

estudanteIFC = ClasseEstudante.Estudante("Leonardo", 1828, "21/09/2000")    #self ja vem do ESTUDANTE
estudanteIFC.alterarNome("Felipe")

#estudanteUnifebe = ClasseEstudante.Estudante()
#estudanteUnifebe.alterarNome("Carla")
#estudanteUnifebe.nome = "Carla"

nomeIFC = estudanteIFC.mostrarNome()
print(f"Mostrar nome estudante do IFC: {nomeIFC}")
#print do estudante do ifc que recebeu nome. 

#nomeUnifebe = estudanteUnifebe.mostrarNome()
#print(f"Mostrar nome estudante da Unifebe: {nomeUnifebe}")
#print(f"Estudante da Unifebe: {estudanteUnifebe.nome}.")
#print do estudante da Unifebe que recebeu nome.

#A idéia de você isolar totalmente as variáveis dentro da classe.
#Controle total e absoluto de tudo doque acontece dentro da classe. 
#Quando a classe estiver pronta a idéia é de que ela esteja blindade, e que não seja nunca mais modificada.
#Proteger as variáveis de receber valores diretamente do programa principal.

#pass segue o código