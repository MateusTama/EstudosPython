from flask import Flask, render_template

app = Flask(__name__)

###############################################################
#@app.route('/')
#def home():
#    clubes = [clubes, professores, estudantes]
#    conteudo = render_template('index.html', parClubes=clubes)
#    return conteudo
###############################################################
#@app.route("/rotaDinamica")
#def rotaPadrao():
#    valor = "Conselho de classe amanhã"
#   conteudo = render_template("rotaDinamica.html", parValor=valor)
#    return conteudo

#@app.route("/rotaDinamica/<valor>")
#def rotaDinamica(valor):
#    conteudo = render_template(".html", parValor=valor)
#    return conteudo
##############################################################

@app.route("/clube/<nomeDoClube>")
def clube(parNomeProf):
    nomeDoClube = ['teatro','musica','jogos' ]
    professorResponsavel = parNomeProf
    conteudo = render_template("clube.html", parNomeClub=nomeDoClube, parNomeProf = professorResponsavel)
    return conteudo

@app.route("/estudantes")
def estudantes():
    nome = ["Miguel","Arthur","Gael","Théo","Heitor","Ravi","Davi" ,"Bernardo"]
    turma = ["2ºinfo a", "3ºinfo a","2ºinfo a", "3ºinfo a","2ºinfo a", "3ºinfo a","2ºinfo a", "3ºinfo a","2ºinfo a", "3ºinfo a","2ºinfo a", "3ºinfo a"]
    conteudo = render_template("clube.html", parNomEstudante=nome, parTurma = turma)
    return conteudo

@app.route("/professores")
def professores():
    nome = ['andré','lucas','pedro','andreça']
    disciplina = ['musica','teatro','jogos','dança']
    conteudo = render_template("clube.html", parNomeProf=nome, parDisciplina = disciplina)
    return conteudo

def adicionarMembro(parNomEstudante,clubesdosmembros):
    membros = [teatro,musica,jogos] 
    teatro = ["Miguel","Arthur","Gael"]
    musica = ["Théo","Heitor"]
    jogos = ["Ravi","Davi" ,"Bernardo"]

    conteudo = render_template("clube.html", parNomeClub=membros)
    return conteudo

if __name__ == '__main__':
    app.run(debug=True)
