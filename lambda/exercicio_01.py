"""
Escreva uma função lambda que retorne o dobro de um número
"""


def executa(funcao, *args):
    return funcao(*args)


numero = int(input('Digite um número: '))
dobro = executa(lambda x, y: x * y, numero, 2)
print(f'O dobro do número {numero} é {dobro}.')
