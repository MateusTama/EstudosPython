#PROXIMO PASSO, INSERIR IMAGENS E FAZER UPLOAD COM FLASK (IMAGENS PARA SERIE)

from flask import Flask, render_template, request, session
# render_template para carregar arquivos html pelo flask
# request para poder pegar os dados de formulário
# session para poder guardar valores nas variáveis de sessão do navegador da pessoa
from classes import Serie, Tema
from random import choice

app = Flask(__name__)
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

catalogo = [tema_suspense, tema_policial, tema_drama]

### FIM DA CRIAÇÃO DOS OBJETOS ###

@app.route('/')
def home():
    # SE A CHAVE "login" NÃO EXISTIR DENTRO DO DICIONÁRIO session...
    if "login" not in session:
        # cria a chave "login" na session e coloca o valor False
        session["login"] = False

    #Seleção aleatória de uma série
    #Erro de temas sem séries nenhumas
    # serieDestaque = choice(choice(catalogo).series)

    #RESOLVENDO O ERRO

    #Escolhe um tema do catalogo
    temaDestaque = choice(catalogo)
    #Enquanto não tiver séries na lista de séries do tema, escolhe outro tema
    while len(temaDestaque.series) == 0:
        temaDestaque = choice(catalogo)

    #Seleção aleatória de uma série do tema escolhido
    serieDestaque = choice(temaDestaque.series)

    # chamar a template index.html passando pra ela a série destaque e o catálogo 
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
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
            conteudo = render_template("dashboard.html",parCatalogo=catalogo)
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
        conteudo = render_template("dashboard.html",parCatalogo=catalogo)
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

    #Escolhe um tema do catalogo
    temaDestaque = choice(catalogo)
    #Enquanto não tiver séries na lista de séries do tema, escolhe outro tema
    while len(temaDestaque.series) == 0:
        temaDestaque = choice(catalogo)

    #Seleção aleatória de uma série do tema escolhido
    serieDestaque = choice(temaDestaque.series) 

    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo

# TEMAS

@app.route("/modificar_tema/<nome_do_tema>")
def modificar_tema(nome_do_tema):
    #Se o usuario estiver logado chama o modificar_tema.html com o tema dinâmico
    if session["login"] == True:
        #CASO O TEMA NÃO EXISTA E TENTE ENTRAR PELA URL
        contadorTema = 0
        for tema in catalogo:
            contadorTema += 1
            #Se encontrar o tema, mostra ele e para o for
            if nome_do_tema == tema.nome:
                conteudo = render_template('modificar_tema.html', parNomeTema=nome_do_tema)
                break

            #Caso não encontrar o tema, e acabar os temas do catalogo, mostra uma mensagem avisando que o tema não existe
            elif nome_do_tema != tema.nome and len(catalogo) == contadorTema:
                mensagem = "Esse tema não existe, para criá-lo, acesse o gerenciador."
                conteudo = render_template("mensagem.html", parMensagem=mensagem)
            
            else:
                pass

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
        #Se for True tem tema repetido, se for False não tem tema repetido
        temaRepetido = False
        #Verificar se já está no fim da lista de temas
        indice = 0
        for tema in catalogo:
            indice += 1
            #Se o tema já tiver sido criado (2 temas com o mesmo nome)
            if nome_tema == tema.nome:
                temaRepetido = True
                mensagem = "Não é permitido 2 temas com o mesmo nome."
                conteudo = render_template("mensagem.html", parMensagem=mensagem)

            #Não tem tema repetido e já está no fim da lista
            elif temaRepetido==False and indice==len(catalogo):
                novo_tema = Tema(nome_tema)
                catalogo.append(novo_tema)
                conteudo = render_template("dashboard.html", parCatalogo=catalogo)  
                #break pois, se entrar no elif ele adiciona mais um item no catalogo, fazendo o for percorrer a lista do catalogo mais uma vez, podendo gerar loop infinito
                break
    
    #NÃO PREENCHEU O NOME DO NOVO TEMA
    elif session["login"] == True and request.method == "POST" and request.form["nome_tema"] == "":
        mensagem = 'Preencha o campo "Novo nome". O tema não foi criado.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    #Entrou por GET
    elif request.method == "GET":
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    
    else:
        conteudo = render_template("dashboard.html", parCatalogo=catalogo)

    return conteudo

@app.route("/processar_tema/<nome_do_tema>", methods=["GET","POST"])
def processar_tema(nome_do_tema):
    if session["login"] == True and request.method == "POST":
        #Formulário para atualizar nome do tema
        novoNomeTema = request.form["atualizar_nome_tema"]
        for tema in catalogo:
            #Testa qual tema vai atualizar
            if tema.nome==nome_do_tema:
                #atualiza nome
                tema.nome = novoNomeTema 
                #atualiza o nome do tema (url_for e a váriavel)
                #Já atualiza o nome_do_tema recebido para mostrar no template HTML
                nome_do_tema = request.form["atualizar_nome_tema"]
                conteudo = render_template("modificar_tema.html", parNomeTema=nome_do_tema)

    #Entrou por GET
    elif request.method == "GET" and session["login"] == False:
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    elif request.method == "GET" and session["login"] == True:
        mensagem = "Acesso Negado. Entre pelo gerenciador."
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    return conteudo

@app.route("/excluir_tema/<nome_do_tema>", methods=["GET","POST"])
def excluir_tema(nome_do_tema):

    #CONTINUAR PROTEGENDO
    indice = 0
    for tema in catalogo:
        indice+=1
        if nome_do_tema == tema.nome:
            catalogo.pop(indice-1)

    #PROTEGER

    conteudo = render_template("dashboard.html", parNomeTema=nome_do_tema, parCatalogo=catalogo)
    return conteudo

#  A lista de temas é uma lista de links. Mostre os temas existentes como links para 
# /modificar_tema/<nome_do_tema> (use url_for com o parâmetro nome_do_tema). 
# - Ainda nessa página, abaixo da lista de temas, inclua um formulário com um campo de texto 
# para adicionar novos temas. Action desse formulário: /adicionar_tema. 
# - Na rota adicionar_tema no programa principal, crie um novo objeto tema e inclua no catálogo

#SÉRIE

@app.route("/modificar_serie/<titulo_da_serie>", methods=["GET","POST"])
def modificar_serie(titulo_da_serie):
    conteudo = render_template("modificar_serie.html", parTituloSerie=titulo_da_serie)
    return conteudo

@app.route("/processar_serie/<titulo_da_serie>", methods=["GET","POST"])
def processar_serie(titulo_da_serie):
    if request.method == "POST":
        #Formulário para atualizar o titulo da serie
        novoTituloSerie = request.form["atualizar_titulo_serie"]
        for tema in catalogo:
            for serie in tema.series:
            #Testa qual serie vai atualizar
                if serie.titulo==titulo_da_serie:
                    #atualiza serie
                    serie.titulo = novoTituloSerie 
                    #atualiza o nome do tema (url_for e a váriavel)
                    titulo_da_serie = request.form["atualizar_titulo_serie"]
    
    #PROTEGER CONTRA GET

    conteudo = render_template("modificar_serie.html", parTituloSerie=titulo_da_serie)
    return conteudo

    #PROTEGER

@app.route("/adicionar_serie", methods=["GET","POST"])
def adicionar_serie():
    #Enviou o formulário e quer adicionar uma nova serie
    titulo_serie = request.form["titulo_serie"]
    if request.method == "POST" and request.form["titulo_serie"] != "":
        #Se for True tem serie repetida, se for False não tem serie repetida
        serieRepetida = False
        #Verificar se já está no fim da lista de serie
        contadorTema = 0
        for tema in catalogo:
            contadorSerie=0
            contadorTema+=1
            if len(tema.series) == 0:
                #O TEMA NÃO POSSUI SERIES
                temaEscolhido = request.form["tema_serie"]
                #BUSCA O TEMA A PARTIR DO NOME
                if temaEscolhido == tema.nome:
                    #PASSAR INFORMAÇÕES
                    #titulo, imagem, sinopse, temporadas, avaliacao, elenco
                    #DARK.JPG COMO IMAGEM PADRAO
                    serieAdicionada = Serie(request.form["titulo_serie"],"dark.jpg",request.form["sinopse_serie"],request.form["temporadas_serie"],request.form["avaliacao_serie"],request.form["elenco_serie"])
                    #TEMA ESCOLHIDO ADICIONA A SERIE
                    tema.adicionar_serie(serieAdicionada)
                    conteudo = render_template("dashboard.html", parCatalogo=catalogo)
                    break
                
            elif len(tema.series) >= 1:
                for serie in tema.series:
                    contadorSerie += 1
                    if serie.titulo == titulo_serie:
                        serieRepetida = True
                        mensagem = "Não é permitido 2 séries com o mesmo nome"
                        conteudo = render_template("mensagem.html", parMensagem=mensagem)
                        break

                    elif serieRepetida==False and contadorTema==len(catalogo) and contadorSerie==len(tema.series):
                        #NÃO PRECISA PASSAR TEMA
                        temaEscolhido = request.form["tema_serie"]
                        for tema in catalogo:
                            #BUSCA O TEMA A PARTIR DO NOME
                            if temaEscolhido == tema.nome:
                                #PASSAR INFORMAÇÕES
                                #titulo, imagem, sinopse, temporadas, avaliacao, elenco
                                serieAdicionada = Serie(request.form["titulo_serie"],"dark.jpg",request.form["sinopse_serie"],request.form["temporadas_serie"],request.form["avaliacao_serie"],request.form["elenco_serie"])
                                #TEMA ESCOLHIDO ADICIONA A SERIE
                                tema.adicionar_serie(serieAdicionada)
                                conteudo = render_template("dashboard.html", parCatalogo=catalogo)
                                break

                            else:
                                mensagem = "Ocorreu um erro ao adicionar a série."
                                conteudo = render_template("mensagem.html", parMensagem=mensagem)

    elif request.method == "POST" and request.form["titulo_serie"] == "":
        mensagem = 'Preencha o campo "Novo título". A série não foi criada.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    elif request.method == "GET":
        mensagem = 'Acesso negado. Faça login na aba "Início" para poder fazer modificações.'
        conteudo = render_template("mensagem.html", parMensagem=mensagem)
    
    else:
        conteudo = render_template("dashboard.html", parCatalogo=catalogo)

    #PROTEGER CONTRA GET

    return conteudo

@app.route("/excluir_serie/<titulo_da_serie>", methods=["GET","POST"])
def excluir_serie(titulo_da_serie):
    #Cada tema
    for tema in catalogo:
        #funcao que remove a serie a partir do titulo
        tema.removerSerie(titulo_da_serie)

    #PROTEGER

    conteudo = render_template("dashboard.html", parTituloSerie=titulo_da_serie, parCatalogo=catalogo)
    return conteudo

# EXECUTAR O PROGRAMA (RODAR O SITE)
if __name__ == '__main__':
    app.run(debug=True)
