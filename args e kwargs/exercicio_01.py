"""
Escreva uma função chamada soma_args que receba uma quantidade
variável de argumentos numéricos e retorne a soma de todos eles.
"""


def soma_args(*args):
    return sum(*args)


lista = []
condicao = True
while condicao:
    numero = int(input('Digite um número (para sair, digite "-1"): '))
    if numero == -1:
        condicao = False
    else:
        lista.append(numero)

print(f'A soma de todos os números digitados é {soma_args(lista)}')
