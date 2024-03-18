# Identificar padrões de caracteres dentro de strings
# Documentação oficial: https://docs.python.org/pt-br/3.12/library/re.html
# Introdução a documentação: https://docs.python.org/pt-br/3/howto/regex.html#
import re

# findall = Todas as ocorrências do padrão 
# search = Primeira ocorrência do padrão
# sub = substituir uma ocorrência do texto
# compile = compilar regex

# Letras maiúsculas x minúsculas
string = "Primeira vez testando expressões vez regulares"
# Utilizando string literal
print(re.search(r'testando', string)) # Retorna None ou o índice de ocorrência da palavra procurada
print(re.findall(r'vez', string)) # Retorna uma lista vazia ou uma lista com todas as ocorrência da palavra procurada
print(re.sub(r'vez', 'substituindo', string, count=1)) # Substituindo a palavra por outra na string. Por padrão substituímos todas as ocorrências.

# Reutilizando expressões regulares

regex_compile = re.compile(r'vez')
print(regex_compile.search(string))
print(regex_compile.findall(string))
print(regex_compile.sub('1234', string))