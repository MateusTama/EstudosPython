#Nome: Mateus Tamasia, Lucas da Silva Valim e Eduardo Kohler

#PROXIMO PASSO, INSERIR IMAGENS E FAZER UPLOAD COM FLASK (IMAGENS PARA SERIE) 
#UTILIZAR AS CLASSES E FUNCOES (ORGANIZAR)
#Biblioteca do sistema
import os

from werkzeug.utils import secure_filename

from flask import Flask, render_template, request, session
# render_template para carregar arquivos html pelo flask
# request para poder pegar os dados de formulário
# session para poder guardar valores nas variáveis de sessão do navegador da pessoa
from classes import Serie, Tema, Catalogo
from random import choice

#Pasta de upload para as imagens
#getcwd = pega o diretótio onde está o arquivo atual (main.py)
#os.path.join = juntar 2 caminhos ou mais
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/images')

#Dicionário com as extensões permitidas para upload
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
#Configuração da pasta de UPLOAD_FOLDER para o FLASK
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#Tamanho máximo permitido é 10 megabytes
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000

# chave para criptografar as variáveis de sessão
app.secret_key = "LGBSBGKYW#TBRjGJKgkejhrg"

### CRIAÇÃO DOS OBJETOS ###
# considere que todos os objetos "temas" e "series" foram criados corretamente
tema_suspense = Tema("Suspense")

serie_stranger_things = Serie("Stranger Things", "strangerthings.jpg", "Quando Will Byers desaparece misteriosamente, seus amigos iniciam uma busca pelo garoto, descobrindo experimentos secretos, forças sobrenaturais e uma garota estranha com poderes telecinéticos.", 4, "4.5 estrelas", "Millie Bobby Brown, Finn Wolfhard")
tema_suspense.adicionar_serie(serie_stranger_things)

serie_dark = Serie("Dark", "dark.jpg", "Em uma cidade pequena, desaparecimentos inexplicáveis ​​levam quatro famílias a uma busca frenética por respostas enquanto tentam desvendar um mistério que abrange três gerações.", 3, "4.8 estrelas", "Louis Hofmann, Oliver Masucci")
tema_suspense.adicionar_serie(serie_dark)

serie_narcos = Serie("Narcos", "narcos.jpg", "Baseada na história real do narcotraficante Pablo Escobar, essa série retrata a vida do poderoso chefão do tráfico e as forças policiais e políticas que tentam capturá-lo.", 5, "4.7 estrelas", "Wagner Moura, Pedro Pascal")
tema_suspense.adicionar_serie(serie_narcos)

tema_policial = Tema("Policial")

serie_lupin = Serie("Lupin", "lupin.jpg", "Em Paris, o ladrão profissional Assane Diop busca vingança pelo injusto tratamento de seu pai, e usa as habilidades de ladrão para expor os crimes da elite.", 2, "4.6 estrelas", "Omar Sy, Ludivine Sagnier")
tema_policial.adicionar_serie(serie_lupin)

serie_casa_de_papel = Serie("La Casa de Papel", "lacasadepapel.jpeg", "Oito ladrões fazem reféns e se trancam na Casa da Moeda da Espanha com o ambicioso plano de realizar o maior roubo da história.", 5, "4.9 estrelas", "Úrsula Corberó, Álvaro Morte")
tema_policial.adicionar_serie(serie_casa_de_papel)

tema_drama = Tema("Drama")

serie_breaking_bad = Serie("Breaking Bad", "breakingbad.jpg", "Um professor de química do ensino médio com câncer terminal se junta a um ex-aluno para produzir e vender metanfetamina para garantir o futuro financeiro de sua família.", 6, "4.9 estrelas", "Bryan Cranston, Aaron Paul")
tema_drama.adicionar_serie(serie_breaking_bad)

serie_ozark = Serie("Ozark", "ozark.jpg", "Um consultor financeiro se muda com sua família para as montanhas Ozark para lavar 500 milhões de dólares e acalmar um traficante de drogas.", 4, "4.7 estrelas", "Jason Bateman, Laura Linney")
tema_suspense.adicionar_serie(serie_ozark)

serie_the_witcher = Serie("The Witcher", "witcher.jpg", "Um caçador de monstros solitário luta para encontrar seu lugar em um mundo onde as pessoas frequentemente se provam mais perversas do que as bestas.", 2, "4.6 estrelas", "Henry Cavill, Anya Chalotra")
tema_suspense.adicionar_serie(serie_the_witcher)

serie_the_crown = Serie("The Crown", "thecrown.jpg", "Esta série dramática segue a vida da rainha Elizabeth II desde sua juventude até a atualidade, explorando os eventos históricos que moldaram o segundo reinado mais longo da história britânica.", 5, "4.8 estrelas", "Olivia Colman, Tobias Menzies")
tema_drama.adicionar_serie(serie_the_crown)

serie_gambito = Serie("O Gambito da Rainha", "gambito.jpg", "Em um orfanato dos anos 1950, uma jovem prodígio do xadrez luta contra o vício enquanto enfrenta os melhores jogadores do mundo.", 1, "4.5 estrelas", "Anya Taylor-Joy, Bill Camp")
tema_drama.adicionar_serie(serie_gambito)

serie_suits = Serie("Suits", "suits.jpg", "Mike Ross, um jovem inteligente que abandonou a faculdade de direito, é contratado pelo advogado mais bem-sucedido de Nova York, Harvey Specter, apesar de não ter diploma de direito.", 9, "4.7 estrelas", "Gabriel Macht, Patrick J. Adams")
tema_drama.adicionar_serie(serie_suits)

catalogo = Catalogo()
catalogo.adicionarTema(tema_suspense)
catalogo.adicionarTema(tema_drama)
catalogo.adicionarTema(tema_policial)

### FIM DA CRIAÇÃO DOS OBJETOS ###

@app.route('/')
def home():
    # SE A CHAVE "login" NÃO EXISTIR DENTRO DO DICIONÁRIO session...
    if "login" not in session:
        # cria a chave "login" na session e coloca o valor False
        session["login"] = False

    serieDestaque = catalogo.escolherSerieDestaque()

    # chamar a template index.html passando pra ela a série destaque e o catálogo 
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo.temas)
    return conteudo

# como essa rota pode chegar vinda de um formulário, precisamos ativar os métodos 
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # pode chegar nessa rota vindo de um formulário ou vindo de um link.
    # quando chegar nessa rota vindo de um formulário:
    if request.method == "POST":
        # vamos pegar o que foi preenchido no formulário
        # os campos do formulário ficam armazenados no dicionário request.form
        # as chaves do dicionário são os "name" dos campos do form na template
        # os valores do dicionário são as respostas que a pessoa preencheu nos campos
        if request.form["email"] == "eu@eu.com" and request.form["senha"] == "aaa":
            # Se a pessoa acertar o login, vai alterar a session "login" para True
            # Assim saberemos em qualquer página do site se a pessoa fez login ou não
            session["login"]=True
            # depois do login, chamamos o painel de gerenciamento passando pra ele o catálogo
            conteudo = render_template("dashboard.html",parCatalogo=catalogo.temas)
        else:
            # Se errar o login:
            mensagem = "Login inválido."
            # chamamos o template de mensagem pra mostrar uma mensagem de erro
            conteudo = render_template("mensagem.html", parMensagem=mensagem)
    
    # esse elif pertence ao primeiro IF dessa def
    # quando chegar nessa rota via GET (por um link por exemplo) 
    # mas já ter feito login:
    elif request.method == "GET" and session["login"] == True:        
        # se já fez login pode acessar o painel de gerenciamento
        conteudo = render_template("dashboard.html",parCatalogo=catalogo.temas)
    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode acessar o painel, 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    # depois dos testes de login vai retornar o conteúdo correto:
    return conteudo

@app.route("/logout")
def logout():
    # primeiro verificamos se existe algum login na session
    # caso seja o primeiro acesso ao site e a pessoa digite o endereço do logout,
    # não vai ter a chave "login" dentro da session para alterar.

    # se a chave "login" existir dentro da session...
    if "login" in session:
        # altera o valor de "login" na session e coloca o valor False
        # isso vai efetivar o logout
        session["login"] = False   

    #Seleção aleatória de uma série
    #Erro de temas sem séries nenhumas
    # serieDestaque = choice(choice(catalogo).series)

    #RESOLVENDO O ERRO

    serieDestaque = catalogo.escolherSerieDestaque()

    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo.temas)
    return conteudo

# TEMAS

@app.route("/modificar_tema/<nome_do_tema>")
def modificar_tema(nome_do_tema):
    #Se o usuario estiver logado chama o modificar_tema.html com o tema dinâmico
    if session["login"] == True:
        conteudo = catalogo.modificarTema(nome_do_tema)

    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar temas 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    return conteudo

#ROTA CASO ESQUEÇA DE ESPECIFICAR O TEMA NA URL
@app.route("/modificar_tema")
def erroModificarTema():
    if session["login"] == True:
        mensagem = "Para poder modificar o tema é necessário especificá-lo na URL. Exemplo: /modificar_tema/nome_do_tema"
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar temas 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    return conteudo

@app.route("/adicionar_tema", methods=["GET","POST"])
def adicionar_tema():
    #ERRO DE FICAR DANDO REFRESH NA PAGINA E ENVIANDO O FORMULÁRIO NOVAMENTE
    #Enviou o formulário e quer adicionar um novo tema
    #SE O FORMULÁRIO NÃO FOR ENVIADO VAZIO

    if session["login"] == True and request.method == "POST" and request.form["nome_tema"] != "":
        nome_tema = request.form["nome_tema"]
        conteudo = catalogo.adicionarTemaFlask(nome_tema)
    
    #NÃO PREENCHEU O NOME DO NOVO TEMA
    elif session["login"] == True and request.method == "POST" and request.form["nome_tema"] == "":
        mensagem = 'Preencha o campo "Novo nome". O tema não foi criado.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    #Entrou por GET
    elif request.method == "GET":
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    
    else:
        conteudo = render_template("dashboard.html", parCatalogo=catalogo.temas)

    return conteudo

@app.route("/processar_tema/<nome_do_tema>", methods=["GET","POST"])
def processar_tema(nome_do_tema):
    if session["login"] == True and request.method == "POST":
        #Atualizar nome do tema
        novoNomeTema = request.form["atualizar_nome_tema"]
        conteudo = catalogo.atualizarNomeTema(nome_do_tema, novoNomeTema)

    #Entrou por GET
    elif request.method == "GET" and session["login"] == False:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    elif request.method == "GET" and session["login"] == True:
        mensagem = "Acesso Negado. Entre pelo gerenciador."
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    return conteudo

#TENTAR ENTRAR PELA URL
@app.route("/processar_tema")
def erroProcessarTema():
    if session["login"] == True:
        mensagem = "Acesso Negado. Entre pelo gerenciador."
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar temas 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    return conteudo

@app.route("/excluir_tema/<nome_do_tema>", methods=["GET","POST"])
def excluir_tema(nome_do_tema):
    #Excluiu através do formulário e está logado
    if request.method == "POST" and session["login"] == True:
        conteudo = catalogo.excluirTema(nome_do_tema)
    
    elif request.method == "GET" and session["login"] == True:
        mensagem = "Acesso Negado. Acesse está página pelo link do tema."
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    
    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar temas 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    return conteudo

#  A lista de temas é uma lista de links. Mostre os temas existentes como links para 
# /modificar_tema/<nome_do_tema> (use url_for com o parâmetro nome_do_tema). 
# - Ainda nessa página, abaixo da lista de temas, inclua um formulário com um campo de texto 
# para adicionar novos temas. Action desse formulário: /adicionar_tema. 
# - Na rota adicionar_tema no programa principal, crie um novo objeto tema e inclua no catálogo

#SÉRIE

#TERMINAR

@app.route("/modificar_serie/<titulo_da_serie>", methods=["GET","POST"])
def modificar_serie(titulo_da_serie):
    if session["login"] == True:
        conteudo = catalogo.modificarSerie(titulo_da_serie)

    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar series
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    return conteudo

#ROTA CASO ESQUEÇA DE ESPECIFICAR A SÉRIE NA URL
@app.route("/modificar_serie")
def erroModificarSerie():
    if session["login"] == True:
        mensagem = "Para poder modificar a série é necessário especificá-la na URL. Exemplo: /modificar_serie/titulo_da_serie"
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar series
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    return conteudo

@app.route("/processar_serie/<titulo_da_serie>", methods=["GET","POST"])
def processar_serie(titulo_da_serie):
    if request.method == "POST" and session["login"] == True:
        #Formulário para atualizar o titulo da serie
        tituloSerieNovo = request.form["atualizar_titulo_serie"]
        tituloSerieAntigo = titulo_da_serie
        conteudo = catalogo.atualizarSerie(tituloSerieNovo, tituloSerieAntigo)

    #Entrou por GET
    elif request.method == "GET" and session["login"] == False:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    elif request.method == "GET" and session["login"] == True:
        mensagem = "Acesso Negado. Entre pelo gerenciador."
        conteudo = render_template("mensagem.html", parMensagem=mensagem)


    return conteudo

#TENTAR ENTRAR PELA URL
@app.route("/processar_serie")
def erroProcessarSerie():
    if session["login"] == True:
        mensagem = "Acesso Negado. Entre pelo gerenciador."
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar temas 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    return conteudo

@app.route("/adicionar_serie", methods=["GET","POST"])
def adicionar_serie():
    #Enviou o formulário e quer adicionar uma nova serie
    #
    if request.method == "POST" and request.form['titulo_serie'] != "" and session["login"] == True:
        #Caso não tenha nenhum tema no catalogo
        if len(catalogo.temas) == 0:
            mensagem = 'O catalogo não possui nenhum tema. Adicione um tema para poder adicionar uma série.'
            conteudo = render_template("mensagem.html", parMensagem=mensagem)

        elif len(catalogo.temas) >= 1:
            # titulo, imagem, sinopse, temporadas, avaliacao, elenco
            titulo_serie = request.form["titulo_serie"]
            temaEscolhido = request.form["tema_serie"]
            sinopse = request.form["sinopse_serie"]
            temporadas = request.form["temporadas_serie"]
            avaliacao = request.form["avaliacao_serie"]
            elenco = request.form["elenco_serie"]
            #PEGA O ARQUIVO DA IMAGEM INSERIDO NO FORMULÁRIO
            imagem = request.files["imagem_serie"]
            #Se não tiver imagem vai ser definida como a imagem da série dark
            if imagem.filename == '':
                nomeImagem = "dark.jpg"
            else:
                #.filename = pega o nome da imagem
                #secure_filename(evita que o nome da imagem, seja algo como: /../../../home/username) 
                nomeImagem = secure_filename(imagem.filename)           
                #Salvar a imagem(arquivo request.files), através da biblioteca os (sistema), com o submódulo path (pasta) e com o método join (juntando 2 caminhos, UPLOAD_FOLDER + IMAGEM (file) )
                imagem.save(os.path.join(app.config['UPLOAD_FOLDER'], nomeImagem))
            
            conteudo = catalogo.adicionarSerie(titulo_serie, nomeImagem, sinopse, temporadas, avaliacao, elenco, temaEscolhido)
        

    #fazer elif com or para cada campo não preenchido
    elif request.method == "POST" and request.form["titulo_serie"] == "" and session["login"] == True:
        mensagem = 'Preencha o campo "Título". A série não foi criada.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    else:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    return conteudo

@app.route("/excluir_serie/<titulo_da_serie>", methods=["GET","POST"])
def excluir_serie(titulo_da_serie):
    if request.method=="POST" and session["login"] == True:
        tituloSerie = titulo_da_serie
        conteudo = catalogo.excluirSerie(tituloSerie)

    elif request.method=="GET" and session["login"] == True:    
        mensagem = "Acesso Negado. Acesse está página pelo link das séries."
        conteudo = render_template("mensagem.html", parMensagem=mensagem)        

    elif session["login"] == False:
        # quando chegar nessa rota sem ter feito login:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        # não pode modificar series
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    return conteudo

# EXECUTAR O PROGRAMA (RODAR O SITE)
if __name__ == '__main__':
    app.run(debug=True)
 