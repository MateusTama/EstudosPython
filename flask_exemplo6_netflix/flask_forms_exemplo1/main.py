from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    conteudo = render_template("index.html")
    return conteudo

@app.route("/usuario", methods = ["GET", "POST"])
def boasVindas():
    respostaNome = request.form["resposta"]
    conteudo = render_template("usuario.html", nomeLogin = respostaNome)
    return conteudo

@app.route("/forms")
def pagina_formulario():
    conteudo = render_template("forms.html")
    return conteudo

@app.route("/processar", methods = ["GET", "POST"])
def processa_formulario():
    conteudo = render_template("processar_form.html")
    return conteudo



if __name__ == "__main__":
    app.run(debug=True)

