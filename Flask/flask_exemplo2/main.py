from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    conteudo = "Bem-vindos ao meu primeiro aplicativo Flask!"
    return conteudo

@app.route('/sobre')
def sobre():
    conteudo = "Este é um aplicativo Flask básico para demonstração."
    return conteudo

if __name__ == '__main__':
    app.run(debug=True)
