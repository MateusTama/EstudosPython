from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    conteudo = """
    <!DOCTYPE=html>
    <html>
        <head>
            <title>Meu primeiro site em Flask</title>
        </head>
        <body>
            <h2>Flask</h2>
            <p>Flask é louco. Quer saber mais? 
                Clique <a href='/sobre'>aqui</a>
            </p>
        </body>
    </html>"""
    return conteudo

@app.route('/sobre')
def sobre():
    conteudo = "Este é um aplicativo Flask básico para demonstração."
    return conteudo

if __name__ == '__main__':
    app.run(debug=True)
