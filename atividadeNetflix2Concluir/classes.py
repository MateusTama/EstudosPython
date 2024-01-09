from random import choice
from flask import Flask, render_template

class Serie:
    def __init__(self, titulo, imagem, sinopse, temporadas, avaliacao, elenco):
        self.titulo = titulo
        self.imagem = imagem
        self.sinopse = sinopse
        self.temporadas = temporadas
        self.avaliacao = avaliacao
        self.elenco = elenco

class Tema:
    def __init__(self, nome):
        self.nome = nome
        self.series = []

    def adicionar_serie(self, serie):
        self.series.append(serie)

class Catalogo:
    def __init__(self):
        self.temas = []

    def escolherSerieDestaque(self):
        #Seleção aleatória de uma série
        #Erro de temas sem séries nenhumas
        #serieDestaque = choice(choice(catalogo).series)
        #RESOLVENDO O ERRO
        #Escolhe um tema do catalogo
        temaDestaque = choice(self.temas)
        #Enquanto não tiver séries na lista de séries do tema, escolhe outro tema
        while len(temaDestaque.series) == 0:
            temaDestaque = choice(self.temas)
        #Seleção aleatória de uma série do tema escolhido
        serieDestaque = choice(temaDestaque.series)
        return serieDestaque
    
    def adicionarTema(self, parTema):
        self.temas.append(parTema)

    def adicionarTemaFlask(self, nome_tema):
        #SE NÃO TIVER NENHUM TEMA NA LISTA
        #Se for True tem tema repetido, se for False não tem tema repetido
        temaRepetido = False
        serieAdicionada = False
        #Verificar se já está no fim da lista de temas
        indice = 0
        if len(self.temas) == 0:
            serieAdicionada = True
            novo_tema = Tema(nome_tema)
            self.adicionarTema(novo_tema)
            conteudo = render_template("dashboard.html", parCatalogo=self.temas)  
            #break pois, se entrar no elif ele adiciona mais um item no catalogo, fazendo o for percorrer a lista do catalogo mais uma vez, podendo gerar loop infinito

        elif len(self.temas) >= 1 and serieAdicionada == False:
            for tema in self.temas:
                indice += 1
                #Se o tema já tiver sido criado (2 temas com o mesmo nome)
                if nome_tema == tema.nome:
                    temaRepetido = True
                    mensagem = "Não é permitido 2 temas com o mesmo nome."
                    conteudo = render_template("mensagem.html", parMensagem=mensagem)

                #Não tem tema repetido e já está no fim da lista
                elif temaRepetido==False and indice==len(self.temas):
                    novo_tema = Tema(nome_tema)
                    self.adicionarTema(novo_tema)
                    conteudo = render_template("dashboard.html", parCatalogo=self.temas)  
                    #break pois, se entrar no elif ele adiciona mais um item no catalogo, fazendo o for percorrer a lista do catalogo mais uma vez, podendo gerar loop infinito
                    break

        return conteudo
    
    def modificarTema(self, parNome_do_tema):
        nome_do_tema = parNome_do_tema
        contadorTema = 0
        for tema in self.temas:
            contadorTema += 1
            #Se encontrar o tema, mostra ele e para o for
            if nome_do_tema == tema.nome:
                conteudo = render_template('modificar_tema.html', parNomeTema=nome_do_tema)
                break

            #CASO O TEMA NÃO EXISTA E TENTE ENTRAR PELA URL
            #Caso não encontrar o tema, e acabar os temas do catalogo, mostra uma mensagem avisando que o tema não existe
            elif nome_do_tema != tema.nome and len(self.temas) == contadorTema:
                mensagem = "Esse tema não existe, para criá-lo, acesse o gerenciador."
                conteudo = render_template("mensagem.html", parMensagem=mensagem)


        return conteudo
    
    def atualizarNomeTema(self, nomeTemaAntigo, nomeTemaNovo):
        #Formulário para atualizar nome do tema
        novoNome = nomeTemaNovo
        nomeAntigo = nomeTemaAntigo
        for tema in self.temas:
            #Testa qual tema vai atualizar
            #lstrip = tira todos os espaços da esquerda
            if novoNome.lstrip() == '':
                mensagem="O tema precisa de um nome para ser adicionado."
                conteudo = render_template("mensagem.html", parMensagem=mensagem)
                break
            elif tema.nome==nomeAntigo:
                #atualiza nome
                tema.nome = novoNome 
                #atualiza o nome do tema (url_for e a váriavel)
                #Já atualiza o nome_do_tema recebido para mostrar no template HTML
                conteudo = render_template("modificar_tema.html", parNomeTema=novoNome)

        return conteudo
    
    def excluirTema(self, parNome_Tema):
        nome_do_tema = parNome_Tema
        for tema in self.temas:
            if nome_do_tema == tema.nome:
                self.temas.remove(tema)
                conteudo = render_template("dashboard.html", parNomeTema=nome_do_tema, parCatalogo=self.temas)
        return conteudo
    
    def modificarSerie(self, parTituloSerie):
        titulo_serie = parTituloSerie
        contadorTema = 0
        serieEncontrada = False
        for tema in self.temas:
            contadorTema += 1
            contadorSerie = 0
            #Se encontrar o tema, mostra ele e para o for
            if len(tema.series) >= 1:
                for serie in tema.series:
                    contadorSerie += 1
                    if titulo_serie == serie.titulo:
                        conteudo = render_template('modificar_serie.html', parTituloSerie=titulo_serie)
                        serieEncontrada = True
                        break
                        #CASO A SÉRIE NÃO EXISTA E TENTE ENTRAR PELA URL
                        #Caso não encontrar a serie, e acabar as séries e os temas do catalogo, mostra uma mensagem avisando que a série não existe
                    elif serieEncontrada==False and titulo_serie != serie.titulo and len(self.temas) == contadorTema and len(tema.series) == contadorSerie:
                        mensagem = "Essa série não existe, para criá-la, acesse o gerenciador."
                        conteudo = render_template("mensagem.html", parMensagem=mensagem)

            elif serieEncontrada==False and len(tema.series) == 0 and len(self.temas) == contadorTema:              
                mensagem = "Essa série não existe, para criá-la, acesse o gerenciador."
                conteudo = render_template("mensagem.html", parMensagem=mensagem)

        return conteudo

    def atualizarSerie(self, tituloSerieNovo, tituloSerieAntigo):
        tituloNovo = tituloSerieNovo
        tituloAntigo = tituloSerieAntigo
        for tema in self.temas:
            for serie in tema.series:
            #Testa qual serie vai atualizar
                #lstrip = tira todos os espaços da esquerda
                if tituloNovo.lstrip() == '':
                    mensagem="A série precisa de um nome para ser adicionado."
                    conteudo = render_template("mensagem.html", parMensagem=mensagem)
                    break
                elif serie.titulo==tituloAntigo:
                    #atualiza serie
                    serie.titulo = tituloNovo
                    #atualiza o nome do tema (url_for e a váriavel)
                    conteudo = render_template("modificar_serie.html", parTituloSerie=tituloNovo)
        return conteudo
    
    def adicionarSerie(self, titulo, imagem, sinopse, temporadas, avaliacao, elenco, temaEscolhido):
        #Se for True tem serie repetida, se for False não tem serie repetida
        titulo_serie = titulo
        nomeImagem = imagem
        sinopse_serie = sinopse
        temporadas_serie = temporadas
        avaliacao_serie = avaliacao
        elenco_serie = elenco
        tema_serie = temaEscolhido
        serieRepetida = False
        #Verificar se já está no fim da lista de serie
        contadorTema = 0
        for tema in self.temas:
            contadorSerie=0
            contadorTema+=1

            if len(tema.series) == 0 and tema_serie == tema.nome:
                #O TEMA NÃO POSSUI SERIES
                #BUSCA O TEMA A PARTIR DO NOME
                #PASSAR INFORMAÇÕES
                serieAdicionada = Serie(titulo_serie, nomeImagem, sinopse_serie, temporadas_serie, avaliacao_serie, elenco_serie)
                #TEMA ESCOLHIDO ADICIONA A SERIE
                tema.adicionar_serie(serieAdicionada)
                conteudo = render_template("dashboard.html", parCatalogo=self.temas)
                break
                
            elif len(tema.series) >= 1:
                for serie in tema.series:
                    contadorSerie += 1
                    if serie.titulo == titulo_serie:
                        serieRepetida = True
                        mensagem = "Não é permitido 2 séries com o mesmo nome"
                        conteudo = render_template("mensagem.html", parMensagem=mensagem)
                        break

                    elif serieRepetida==False and contadorTema==len(self.temas) and contadorSerie==len(tema.series):
                        #NÃO PRECISA PASSAR TEMA
                        for tema in self.temas:
                            #BUSCA O TEMA A PARTIR DO NOME
                            if tema_serie == tema.nome:
                                #PASSAR INFORMAÇÕES
                                #titulo, imagem, sinopse, temporadas, avaliacao, elenco
                                serieAdicionada = Serie(titulo_serie, nomeImagem, sinopse_serie, temporadas_serie, avaliacao_serie, elenco_serie)
                                #TEMA ESCOLHIDO ADICIONA A SERIE
                                tema.adicionar_serie(serieAdicionada)
                                conteudo = render_template("dashboard.html", parCatalogo=self.temas)
                                break

                            else:
                                mensagem = "Ocorreu um erro ao adicionar a série."
                                conteudo = render_template("mensagem.html", parMensagem=mensagem)

            #CASO A ULTIMA SÉRIE DO CATALOGO NÃO TENHA SÉRIES
            elif serieRepetida == False and contadorTema == len(self.temas) and len(tema.series) == 0:
                #NÃO PRECISA PASSAR TEMA
                for tema in self.temas:
                    #BUSCA O TEMA A PARTIR DO NOME
                    if tema_serie == tema.nome:
                        #PASSAR INFORMAÇÕES
                        #titulo, imagem, sinopse, temporadas, avaliacao, elenco
                        serieAdicionada = Serie(titulo_serie, nomeImagem, sinopse_serie, temporadas_serie, avaliacao_serie, elenco_serie)
                        #TEMA ESCOLHIDO ADICIONA A SERIE
                        tema.adicionar_serie(serieAdicionada)
                        conteudo = render_template("dashboard.html", parCatalogo=self.temas)
                        break

        return conteudo

    def excluirSerie(self, tituloSerie):
        #funcao que remove a serie a partir do titulo
        #Cada tema
        titulo_da_serie = tituloSerie
        for tema in self.temas:
            for serie in tema.series:
                if serie.titulo == titulo_da_serie:
                    tema.series.remove(serie)
            conteudo = render_template("dashboard.html", parTituloSerie=titulo_da_serie, parCatalogo=self.temas)

        return conteudo