import json

#STRING JSON PARA DICIONÁRIO PYTHON

#MÉTODO LOAD

input("MÉTODO LOADS - STRING JSON PARA DICIONÁRIO PYTHON. Pressione ENTER")
print()

anime = """{    
    "name": "one-piece",
    "rate": " 9.5",
    "src-img": "https://blkom.com/img/special/3732/gintama-the-semi-final-poster-3767.jpg",
    "description": "حلقات خاصة تمهيدا لأحداث الفيلم الثالث .",
    "episodes": [
            {
                "1": [
                    {
                        "Blkom": "https://cdn2.vid4up.xyz/embedvideo/16016cca62425a"
                    }
                ]
            },
            {
                "2": [
                    {
                        "Blkom": "https://cdn2.vid4up.xyz/embedvideo/16016ccb09d13c"
                    }
                ]
            }
        ]
}"""

#NÃO PODE USAR INDENT, ENSURE_ASCII E SORT_KEYS
anime_dict = json.loads(anime)
print(anime_dict)
print(type(anime_dict)) #DICT
print()

#DICIONÁRIO PYTHON PARA STRING JSON

input("MÉTODO DUMPS - DICIONÁRIO PYTHON PRA STRING JSON. Pressione ENTER")
print()

anime_dicionario = {
    "name": "jujutsu-kaisen",
    "rate": " 9",
    "src-img": "https://blkom.com/img/special/3732/gintama-the-semi-final-poster-3767.jpg",
    "description": "حلقات خاصة تمهيدا لأحداث الفيلم الثالث .",
    "episodes": [
            {
                "1": [
                    {
                        "Blkom": "https://cdn2.vid4up.xyz/embedvideo/16016cca62425a"
                    }
                ]
            },
            {
                "2": [
                    {
                        "Blkom": "https://cdn2.vid4up.xyz/embedvideo/16016ccb09d13c"
                    }
                ]
            }
        ]
}

#PODE USAR INDENT, SORT_KEYS E ENSURE_ASCII
#INDENT = FORMATAR VISUALMENTE
#SORT_KEYS = ORDENAR ALFABETICAMENTE
#ENSURE_ASCII = PADRÃO UTF-8
anime_string = json.dumps(anime_dicionario, indent=4, sort_keys=True, ensure_ascii=False)

print(anime_string)
print(type(anime_string)) #STR
print()

#MÉTODO LOAD - LER ARQUIVOS JSON

input("MÉTODO LOAD - LER ARQUIVOS JSON. Pressione ENTER")
print()

#LÊ O ARQUIVO A PARTIR DO CAMINHO RELATIVO (USAR A BIBLIOTECA os COM O COMANDO os.getcwd() CASO NECESSÁRIO)
#ABRE O JSON COMO A VARIÁVEL file (import pandas as pd)
with open("pythonJSON/BD_animes.json") as file:
    #LÊ A VARIÁVEL CONTENDO O JSON
    #NÃO PODE USAR INDENT, ENSURE_ASCII E SORT_KEYS
    animes = json.load(file)

print(animes)
print(type(animes)) #LIST
print()

#MÉTODO DUMP

input("MÉTODO DUMP - ESCREVER ARQUIVOS JSON. Pressione ENTER")
print()

#ESSE MÉTODO SOBRESCREVE O ARQUIVO, CASO EXISTA ALGO
#CASO O ARQUIVO NÃO EXISTA, O MÉTODO CRIA ESSE ARQUIVO

with open("pythonJSON/new_BD_animes.json", "w") as file:
    json.dump(animes, file)
    print("Adicionado com sucesso.")
    print()

#MANTENDO OS ANIMES ANTERIORES E ADICIONANDO MAIS UM ANIMES
input("MANTENDO OS ANIMES ANTERIORES E ADICIONANDO MAIS UM ANIMES. Pressione ENTER")
print()

#LENDO OS ANIMES ANTIGOS
with open("pythonJSON/new_BD_animes.json") as file:
    todosAnimes = json.load(file) #type=list
    print("Lido com sucesso.")
    print()

#SOBRESCREVENDO OS ANIMES ANTIGOS MAIS O ANIME NOVO
with open("pythonJSON/new_BD_animes.json", "w") as file:
    #append no objeto da linha 13 (ANIME: one-piece)
    #LEMBRAR: NÃO PODE ESTAR NO FORMATO JSON STRING (FAZER loads)
    todosAnimes.append(anime_dict)
    #PODE USAR INDENT, SORT_KEYS E ENSURE_ASCII
    #INDENT = FORMATAR VISUALMENTE
    #SORT_KEYS = ORDENAR ALFABETICAMENTE
    #ENSURE_ASCII = PADRÃO UTF-8
    json.dump(todosAnimes, file, indent=4, ensure_ascii=True)
    print("Sobrescrito com sucesso.")
    print()
