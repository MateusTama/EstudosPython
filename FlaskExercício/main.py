from flask import Flask, render_template
import classes

app = Flask(__name__)

#A rota “/” deve renderizar um template index.html que mostra uma lista de todos
#os clubes, o professor responsável e o horário de reunião de cada clube.
#o A rota dinâmica “/clube/<nomeDoClube>” deve renderizar um template
#clube.html que mostra informações detalhadas sobre o clube selecionado,
#incluindo todos os membros do clube. Note que essa rota é dinâmica e
#depende de qual clube o usuário selecionou.
#o A rota “/professores” deve renderizar um template professores.html que mostra
#uma lista de todos os professores.
#o A rota “/estudantes” deve renderizar um template estudantes.html que mostra
#uma lista de todos os estudantes

estudantes = []
clubes = []
professores = []

estudante1 = classes.Estudante("Bruno","A")
estudantes.append(estudante1)

estudante2 = classes.Estudante("Lucas","B")
estudantes.append(estudante2)

estudante3 = classes.Estudante("Iago","C")
estudantes.append(estudante3)

professor1 = classes.Professor("Leonardo","Programação")
professores.append(professor1)

professor2 = classes.Professor("Tiago", "Física")
professores.append(professor2)

professor3 = classes.Professor("Mirela","Matemática")
professores.append(professor3)

clube1 = classes.Clube("Volei", professor1, "15:30")
clube1.adicionarMembro(estudante1)
clubes.append(clube1)

clube2 = classes.Clube("Futebol", professor2, "13:00")  
clube2.adicionarMembro(estudante2)
clubes.append(clube2)

clube3 = classes.Clube("Basquete", professor3, "9:30")
clube3.adicionarMembro(estudante3)
clubes.append(clube3)

@app.route("/")
def home():
    conteudo = render_template("index.html", parEstudantes = estudantes, parProfessor = professores, parClubes = clubes)
    return conteudo

@app.route("/clube/<nomeDoClube>")
def rotaClube(nomeDoClube):
    conteudo = render_template("clube.html", parNomeDoClube = nomeDoClube, parClube = clubes)
    return conteudo

@app.route("/professores")
def rotaProfessores():
    conteudo = render_template("professores.html", parProfessores = professores)
    return conteudo

@app.route("/estudantes")
def rotaEstudantes():
    clube = "volei"
    conteudo = render_template("estudantes.html", parEstudantes = estudantes)
    return conteudo

if __name__ == "__main__":
    app.run(debug=True)

