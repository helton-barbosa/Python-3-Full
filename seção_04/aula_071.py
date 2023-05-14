"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

print('Uma forma de somar...')


def soma(*args):
    total = 0
    for numero in args:
        total += numero

    return total


retorno = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(retorno)

print('Outra forma de somar...')
numeros = 10, 20, 30, 40, 50, 1, 2, 3, 4, 5
print(numeros, type(numeros))
a = sum(numeros)
print(a)
print(f'Os números são {numeros} e a soma deles é {sum(numeros)}.')
