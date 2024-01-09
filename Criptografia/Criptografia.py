#CRIPTOGRAFAR

criptografia = {}

print()
print("------------------------------------------")
print("---------------CRIPTOGRAFAR---------------")
print("------------------------------------------")
print()

criptografia = { 
               #MINÚSCULA
               "a" : "p", 
               "b" : "a",
               "c" : "z",
               "d" : "i",
               "e" : "b",
               "f" : "y",
               "g" : "e",
               "h" : "r",
               "i" : "m",
               "j" : "l",
               "k" : "n",
               "l" : "g",
               "m" : "j",
               "n" : "c",
               "o" : "w",
               "p" : "o",
               "q" : "v",
               "r" : "f",
               "s" : "k",
               "t" : "q",
               "u" : "s",
               "v" : "t",
               "w" : "h",
               "x" : "u",
               "y" : "x",
               "z" : "d",
               #MAIÚSCULA
               "A" : "P",
               "B" : "A",
               "C" : "Z",
               "D" : "I",
               "E" : "B",
               "F" : "Y",
               "G" : "E",
               "H" : "R",
               "I" : "M",
               "J" : "L",
               "K" : "N",
               "L" : "G",
               "M" : "J",
               "N" : "C",
               "O" : "W",
               "P" : "O",
               "Q" : "V",
               "R" : "F",
               "S" : "K",
               "T" : "Q",
               "U" : "S",
               "V" : "T",
               "W" : "H",
               "X" : "U",
               "Y" : "X",
               "Z" : "D", 
               }

CriMensagem = input("Escreva a mensagem que você deseja criptografar: \n")

print()
print("Pressione ENTER para criptografar...")
input()

msgCriptografada = ""

for CriLetra in CriMensagem:
    if CriLetra in criptografia:
        msgCriptografada += criptografia[CriLetra]
    elif CriLetra == " ":
        msgCriptografada += " "

print(f"Sua mensagem foi criptografada: '{msgCriptografada}'")
print()

print("Pressione ENTER para continuar...")

input()

#DESCRIPTOGRAFAR

descriptografia = {}

print()
print("-----------------------------------------")
print("-------------DESCRIPTOGRAFAR-------------")
print("-----------------------------------------")
print()

descriptografia = {
               #MINÚSCULA
               "p" : "a",
               "a" : "b",
               "z" : "c",
               "i" : "d",
               "b" : "e",
               "y" : "f",
               "e" : "g",
               "r" : "h",
               "m" : "i",
               "l" : "j",
               "n" : "k",
               "g" : "l",
               "j" : "m",
               "c" : "n",
               "w" : "o",
               "o" : "p",
               "v" : "q",
               "f" : "r",
               "k" : "s",
               "q" : "t",
               "s" : "u",
               "t" : "v",
               "h" : "w",
               "u" : "x",
               "x" : "y",
               "d": "z",
               #MAIÚSCULA
               "P" : "A",
               "A" : "B",
               "Z" : "C",
               "I" : "D",
               "B" : "E",
               "Y" : "F",
               "E" : "G",
               "R" : "H",
               "M" : "I",
               "L" : "J",
               "N" : "K",
               "G" : "L",
               "J" : "M",
               "C" : "N",
               "W" : "O",
               "O" : "P",
               "V" : "Q",
               "F" : "R",
               "K" : "S",
               "Q" : "T",
               "S" : "U",
               "T" : "V",
               "H" : "W",
               "U" : "X",
               "X" : "Y",
               "D": "Z",
               }

DesMensagem = input("Escreva a mensagem que você deseja descriptografar: \n")

print()
print("Pressione ENTER para descriptografar...")
input()

msgDescriptografada = ""

for DesLetra in DesMensagem:
    if DesLetra in descriptografia:
        msgDescriptografada += descriptografia[DesLetra]
    elif DesLetra == " ":
        msgDescriptografada += " "

print(f"Sua mensagem foi descriptografada: '{msgDescriptografada}'")
print()

print("FIM.....!!!")
print()
