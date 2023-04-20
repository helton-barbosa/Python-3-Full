"""
Calculadora com While
"""

while True:
    numero_01 = input('Entre com o primeiro número: ')
    numero_02 = input('Entre com o segundo número: ')
    operador = input('Escolha o operador [+ - * /]: ')

    numeros_validos = None

    try:
        num_1_float = float(numero_01)
        num_2_float = float(numero_02)
        numeros_validos = True
    except:
        print('Um ou ambos dos números são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    sair = input('Encerrar? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')

    if sair is True:
        break