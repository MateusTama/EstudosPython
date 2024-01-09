from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    conteudo = "Oi gente, meu primeiro site em Flask"
    return conteudo

if __name__ == "__main__":
    app.run(debug=True)