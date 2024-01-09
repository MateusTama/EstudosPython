from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    mensagem = 'Mensagem para o terceiro ano!'
    conteudo = render_template('index.html', parMensagem=mensagem)
    return conteudo

if __name__ == '__main__':
    app.run(debug=True)
