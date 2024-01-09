from flask import Flask, render_template
import classes

app = Flask(__name__)

# Criar objetos

youtube = classes.Youtube()

canal1 = classes.Canal("Parabólica","Vídeos de História")
video1Canal1 = classes.Video("História do Brasil", "32:55", 500000, 70000, 150)
canal1.adicionarVideos(video1Canal1)
youtube.adicionarCanal(canal1)

canal2 = classes.Canal("Guilherme Freire","Vídeos de Filosofia")
video1Canal2 = classes.Video("Friedrich Nietzche", "20:26", 200000, 40000, 60)
canal2.adicionarVideos(video1Canal2)
video1Canal2.adicionarComentarios("Olá Mundo!")
youtube.adicionarCanal(canal2)

canal3 = classes.Canal("Orochinho","Vídeos de Ironia")
video1Canal3 = classes.Video("Birulinha Cassinos", "19:33", 1000000, 150000, 400)
canal3.adicionarVideos(video1Canal3)
youtube.adicionarCanal(canal3)

# Página Inicial: Exibe uma lista de todos os canais. Ao clicar em um canal, você é
# levado para a página de detalhes do canal.
# • Página de Detalhes do Canal: Mostra informações sobre o canal e uma lista dos
# vídeos postados no canal. Ao clicar em um vídeo, você é levado à página de detalhes
# do vídeo.
# • Página de Detalhes do Vídeo: Exibe detalhes sobre o vídeo, como título, duração,
# quantidade de likes e dislikes, e uma seção para comentários.

# Criando Rotas
# Rota Principal

# Template da página inicial (index.html): 
# o Exibir uma lista dos canais, com o nome do canal, que é um link para a página de 
# detalhes do canal. 
# o Exibir a quantidade total de vídeos presentes em todos os canais. 
# o Parâmetro que deve ser enviado na função render_template: objeto Youtube.

@app.route("/")
def home():
    totalVideos = youtube.totalVideos()
    conteudo = render_template("index.html", parListaCanal = youtube.listaCanal, parTotalVideos = totalVideos)
    return conteudo

# Rota dos Canais

# Template da página de detalhes do Canal (canal.html): 
# o Informações sobre o canal: nome e descrição. 
# o Título da lista: "Vídeos". 
# o Exibir uma lista dos vídeos deste canal, com o título do vídeo (que é um link para 
# a página de detalhes do vídeo), a duração e o número de visualizações. 
# o Parâmetro que deve ser enviado na função render_template: objeto Canal, que 
# contém uma lista de objetos Vídeo.

@app.route("/<parNomeDoCanal>")
def rotaCanal(parNomeDoCanal):
    canal = youtube.buscarCanal(parNomeDoCanal)
    conteudo = render_template("canal.html", parListaVideos = canal.listaVideos ,parNomeDoCanal = parNomeDoCanal, parDescricao = canal.descricao)
    return conteudo

# Rota de Vídeos
# A rota “/video/<nome_video>” deve exibir a página de detalhes do vídeo especificado, 
# com informações sobre o vídeo, como título, duração, quantidade de likes e dislikes, e 
# uma seção para mostrar os comentários. 

# Template da página de detalhes do Vídeo (video.html): 
# o Informações  sobre  o  vídeo:  título,  duração,  número  de  visualizações,  likes, 
# dislikes. 
# o Título da seção: "Comentários". 
# o Exibir uma lista de comentários para este vídeo. 
# o Parâmetro que deve ser enviado na função render_template: objeto Vídeo, que 
# contém uma lista de comentários.

@app.route("/<parNomeDoCanal>/<parNomeDoVideo>")
def rotaVideo(parNomeDoCanal ,parNomeDoVideo):
    canal = youtube.buscarCanal(parNomeDoCanal)
    video = canal.buscarVideo(parNomeDoVideo)
    conteudo = render_template("video.html", parNomeDoCanal = canal.nome ,parNomeDoVideo = video.titulo, parDuracao = video.duracao, parLikes = video.likes, parDislikes = video.dislikes, parComentarios = video.comentarios)
    return conteudo

if __name__ == "__main__":
    app.run(debug=True)