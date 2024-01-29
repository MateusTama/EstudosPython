# https://aprendendo-computacao-com-python.readthedocs.io/en/latest/capitulo_07.html

# String = Dado composto (podemos considerar uma string como algo único ou como algo formado por vários pedaços - caracteres)

# O operador colchete seleciona um único caractere de uma string.:

fruta = "banana"
letra = fruta[1]
print(letra)

# A função len retorna o número de caracteres de uma string:

fruta = "banana"
print(len(fruta))

# Para pegar a última letra de uma string:

comprimento = len(fruta)
print(fruta[comprimento-1])

# Este loop percorre a string e exibe cada letra em sua própria linha. A condição do loop é indice < len(fruta), assim, quando índice é igual ao comprimento da string, a condição se torna falsa, e o corpo do loop não é executado. O último caractere acessado é aquele com o índice len(fruta)-1, que vem a ser o último caractere da string.

indice = 0
while indice < len(fruta):
    letra = fruta[indice]
    print(letra)
    indice = indice + 1

# Como um exercício, escreva uma função que tome uma string como argumento e devolva suas letras de trás para frente, uma por linha.

def reverseString(string):
    for letra in range(0, len(string)):
        letter = string[-letra]
        print(letter)

reverseString("ola123")
        
# A cada vez através do loop, o próximo caractere da string é atribuído à variável char. O loop continua até que não reste mais caracteres.

for char in fruta:
    print(char)

# Naturalmente, esta saída não está cem por cento certa porque “Ouack” e “Quack” estão escritos de maneira errada.

# Como um exercício, modifique o programa para corrigir este erro.
    
prefixos = "JKLMNOPQ"
sufixo = "ack"

for letra in prefixos:
    if letra == "O" or letra == "Q":
        print(letra + "u" + sufixo)
    else:
        print(letra + sufixo)

# Um segmento de uma string é chamado de uma fatia. Selecionar uma fatia é similar a selecionar um caractere:

s = "Pedro, Paulo e Maria"
print(s[0:5])

print(s[7:12])

print(s[15:20])

# Se você omitir o primeiro índice (antes dos dois pontos “:”), a fatia começa do início da string. Se você omitir o segundo índice, a fatia vai até o final da string. Assim:

fruta = "banana"
print(fruta[:3])

print(fruta[3:])

# Mostra a string completa
print(s[:])

# O operador de comparação funciona com strings. Para ver se duas strings são iguais:

palavra = "aaa"

if palavra == "banana":
    print("Sim, nós não temos bananas!")

# Outras operações de comparação são úteis para colocar palavras em ordem alfabética:

# Compara por ordem alfabética

if palavra < "banana":
    print("Sua palavra," + palavra + ", vem antes de banana.")
elif palavra > "banana":
    print("Sua palavra," + palavra + ", vem depois de banana.")
else:
    print("Sim, nós não temos bananas!")

# Entretanto, você deve atentar para o fato de que Pyhton não manipula letras maiúsculas e minúsculas da mesma maneira que as pessoas o fazem. Todas as letras maiúsculas vêm antes das minúsculas. Como resultado:

# Sua palavra, Zebra, vem antes de banana.

# Uma maneira comum de resolver este problema é converter as strings para um formato padrão, seja todas minúsculas, ou todas maiúsculas, antes de realizar a comparação. Um problema mais difícil é fazer o programa perceber que zebras não são frutas.

# É tentador usar o operador [] no lado esquerdo de uma expressão de atribuição, com a intenção de alterar um caractere em uma string. Por exemplo:

saudacao = "Alô, mundo!"
# saudacao[0] = 'E'            
print(saudacao) #ERRO! 

# Strings são imutáveis

# Em vez de produzir a saída Elô, Mundo!, este código produz o erro em tempo de execução (runtime error): TypeError: object doesn't support item assignment (ErroDeTipo: objeto não dá suporte à atribuição de item.)

# Strings são imutáveis, o que significa que você não pode mudar uma string que já existe. O melhor que você pode fazer é criar uma nova string que seja uma variação da original:

saudacao = "Alô, mundo!"
novaSaudacao = 'E' + saudacao[1:]
print(novaSaudacao)

# A solução aqui é concatenar uma nova primeira letra com uma fatia de saudacao. Esta operação não tem nenhum efeito sobre a string original.

# Num certo sentido, find (encontrar) é o oposto do operador []. Em vez de pegar um índice e extrair o caractere correspondente, ela pega um caractere e encontra (finds) em qual índice aquele caractere aparece. Se o caractere não é encontrado, a função retorna -1.

def find(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice = indice + 1
    return -1

# Como um exercício, modifique a função find (encontrar) de modo que ela receba um terceiro parâmetro, o índice da string por onde ela deve começar sua procura.

def find(str, ch, start):
    indice = start
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice = indice + 1
    return -1

# O programa seguinte conta o número e vezes que a letra a aparece em uma string:

fruta = "banana"
contador = 0
for letra in fruta:
  if letra == 'a':
    contador = contador + 1
print(contador)

# Este programa demonstra um outro padrão de computação chamado de contador. A variável contador é inicializada em 0 e então incrementada cada vez que um a é encontrado. (Incrementar é o mesmo que aumentar em um; é o oposto de decrementar, e não tem relação com excremento, que é um substantivo.) Quando se sai do loop, contador guarda o resultado - o número total de a‘s.

# Como um exercício, encapsule este código em uma função chamada contaLetras, e generalize-a de modo que possa aceitar uma string e uma letra como parâmetros.

def contaLetras(str, letraBusca):
    contador = 0
    for letra in str:
        if letra == letraBusca:
            contador = contador + 1
    return contador

print(contaLetras("banana", "n"))

# Como um segundo exercício, reescreva esta função de modo que em vez de percorrer a string, ela use a versão com três parâmetros de find (encontrar) da seção anterior.

def contaLetras(str, ch, start):
    indice = start
    contador = 0
    while indice < len(str):
        if str[indice] == ch:
            contador += 1
        indice = indice + 1
    return contador

print(contaLetras("banana", "a", 0))

# O módulo string contém funções úteis que manipulam strings.

fruta = "pera"

print(str.find(fruta, "e"))

# Além disso, ela recebe um argumento adicional que especifica o índice pelo qual ela deve começar sua procura:

print(str.find("banana", "na", 3))

# Ou ela pode receber dois argumentos adicionais que especificam o intervalo de índices:

print(str.find("bob", "b", 1, 2))
# Se não encontrar retorna -1

# A string string.lowercase contém todas as letras que o sistema considera como sendo minúsculas. Similarmente, string.uppercase contém todas as letras maiúsculas.

print(str.lower(fruta)) #fruta.lower()
print(str.upper(fruta)) #fruta.upper()

# Nós podemos usar essas constantes e find (encontrar) para classificar caracteres. Por exemplo, se find(lowercase, ch) retorna um valor outro que não -1, então ch deve ser minúsculo:

def eMinusculo(ch):
    fruta = "banana"
    return print(fruta.find(ch))

eMinusculo("A")

# Como uma alternativa, podemos tirar vantagem do operador in, que determina se um caractere aparece em uma string:

def eMinusculo(ch):
    fruta = "pera"
    return print(ch in fruta.lower())

eMinusculo("z")

# Ainda, como uma outra alternativa, podemos usar o operador de comparação:

def eMinusculo(ch):
    return print('a' <= ch <= 'z')

eMinusculo("m")
# Se ch estiver entre a e z, ele deve ser uma letra minúscula.

# Como um exercício, discuta que versão de eMinusculo você acha que será a mais rápida. Você pode pensar em outras razões além da velocidade para preferir uma em vez de outra?
# Acredito que utilizando o método IN será mais rápido. Acredito que esse método se supera por ser mais prático
