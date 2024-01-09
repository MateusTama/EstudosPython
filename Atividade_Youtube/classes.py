# Classe Youtube: Funciona como um banco de dados de todos os canais no
# YouTube.
# o Atributos: lista de objetos da classe Canal.
# o Métodos: adicionar novos canais, buscar (e retornar) um canal pelo nome,
# retornar a quantidade total de vídeos (soma dos vídeos de todos os canais).

class Youtube:
    def __init__(self):
        self.listaCanal = []

    def adicionarCanal(self, parCanal):
        self.listaCanal.append(parCanal)

    def buscarCanal(self, parNomeCanal):
        for canal in self.listaCanal:
            if parNomeCanal == canal.nome:
                return canal
                break
    
    def totalVideos(self):
        quantidadeVideos = 0
        for canal in self.listaCanal:
            quantidadeVideos += len(canal.listaVideos)
        return quantidadeVideos

# Classe Canal: Cada objeto Canal representa um canal no YouTube.
# o Atributos: uma lista de Vídeos (cada item na lista de vídeos é um objeto
# Video) e uma descrição.
# o Métodos: um método para adicionar novos vídeos ao canal e outro para
# calcular a quantidade total de likes em todos os vídeos do canal.

class Canal:
    def __init__(self, parNome, parDescricao):
        self.nome = parNome
        self.descricao = parDescricao
        self.listaVideos = []
    
    def adicionarVideos(self, parVideo):
        self.listaVideos.append(parVideo)

    def calcularLikes(self):
        quantidadeLikes = 0
        for video in self.listaVideos:
            quantidadeLikes += self.video.likes
        return quantidadeLikes
    
    def buscarVideo(self, parNomeVideo):
        for video in self.listaVideos:
            if parNomeVideo == video.titulo:
                return video
                break
            

# Classe Video: Cada objeto Video representa um vídeo no YouTube.
# o Atributos: titulo, duracao, visualizações, likes, dislikes e uma lista de
# comentarios.
# o Métodos: adicionar e listar comentários, aumentar likes e aumentar dislikes.

class Video:
    def __init__(self, parTitulo, parDuracao, parVisualizacoes, parLikes, parDislikes):
        self.titulo = parTitulo
        self.duracao = parDuracao
        self.visualizacoes = parVisualizacoes
        self.likes = parLikes
        self.dislikes = parDislikes
        self.comentarios = []

    def adicionarComentarios(self, parComentario):
        self.comentarios.append(parComentario)

    def listarComentarios(self):
        for comentario in self.comentarios:
            print(comentario)

    def aumentarLikes(self):
        self.likes += 1

    def aumentarDislikes(self):
        self.dislikes += 1
