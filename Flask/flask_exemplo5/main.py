from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    itens = ['Item 1', 'Item 2', 'Item 3']
    conteudo = render_template('index.html', parItens=itens)
    return conteudo

if __name__ == '__main__':
    app.run()
