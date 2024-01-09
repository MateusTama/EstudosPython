from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def paginaHome():
    if request.method == "GET":
        conteudo = render_template("home.html", temFilme=False)
    elif request.method == "POST":
        info_filme = request.form
        conteudo = render_template("home.html", temFilme=True, dados=info_filme)
        
    return conteudo

@app.route("/admin")
def paginaAdmin():
    conteudo = render_template("admin.html")
    return conteudo

if __name__ == "__main__":
    app.run(debug=True)




