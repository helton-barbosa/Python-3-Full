"""
Calculadora com While
"""

while True:
    numero_01 = int(input('Entre com o primeiro número: '))
    numero_02 = int(input('Entre com o segundo número: '))

    sair = input('Encerrar? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')

    if sair is True:
        break