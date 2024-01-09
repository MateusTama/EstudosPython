from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    itens = ['Item 1', 'Item 2', 'Item 3']
    conteudo = render_template('index.html', parItens=itens)
    return conteudo

@app.route("/rotaFixa")
def irParaRotaFixa():
    valor = "Conselho de classe hoje"
    conteudo = render_template("rota.html", parValor=valor)
    return conteudo

@app.route("/rotaDinamica/<valor>")
def rotaDinamica(valor):
    conteudo = render_template("rota.html", parValor=valor)
    return conteudo


if __name__ == '__main__':
    app.run(debug=True)
