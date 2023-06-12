"""
Crie uma função chamada concatena_strings que receba uma quantidade variável de "strings"
e retorne a concatenação de todas elas em uma única "string".
"""


def concatena_strings(*args):
    palavra = ''
    for letra in args:
        palavra += letra
    return palavra


lista = []
condicao = True
while condicao:
    letras = input('Digite uma letra (0 para sair): ')
    if letras == '0':
        condicao = False
    else:
        lista.append(letras)

print(concatena_strings(*lista))
