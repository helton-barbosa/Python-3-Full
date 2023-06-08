"""
Escreva uma função lambda que retorne o maior entre dois números
"""


def executa(funcao, *args):
    return funcao(*args)


numero_01 = int(input('Digite o 1º número inteiro: '))
numero_02 = int(input('Digite o 2º número inteiro: '))

resultado = executa(lambda x, y: x if x > y else y, numero_01, numero_02)
print(f'O número maior é {resultado}')
