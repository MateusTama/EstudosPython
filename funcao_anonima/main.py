# Código feito com base em: https://www.youtube.com/watch?v=hZqg9RH5GWk

# Funções anônimas = funções sem nome, em contraste com o def nome_funcao()

# Estrutura: lambda (parametros) parametro_1, parametro_2, parametro_n: (retorno) parametro_1 + parametro_2

# Para utilizar uma função lambda posteriormente atribuímos a uma variável
soma = lambda n1, n2: n1 + n2
# Chamamos a variável que armazena a função lambda
print(soma(3,7))    

# filter

lista = [10,20,30,40,50,60,70,80,90,100]

def acima_de_30(numero):
    return numero > 30

lista_filtrada = list(filter(acima_de_30, lista))
print(lista_filtrada)

# lambda + filter:

lista = [10,20,30,40,50,60,70,80,90,100]

lista_filtrada = list(filter(lambda num: num < 50, lista))
print(lista_filtrada)

