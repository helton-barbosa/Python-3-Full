"""
Faça um programa que peça ao usuário digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite
um número inteiro, informe que não é um número inteiro.
"""
linha_completa = 24 * "#"
linha_partes = 5 * "#"

print(f'{linha_completa}')
print(f'{linha_partes} Par ou Ímpar {linha_partes}')
print(f'{linha_completa}')

valor = input('\nDigite um número inteiro: ')
eh_inteiro = valor.isdigit()

if eh_inteiro:
    valor_2 = int(valor)
    zero = valor_2 == 0
    par = valor_2 % 2 == 0
    if zero:
        print(f'O valor {valor_2} é nulo.')
    elif par:
        print(f'O valor {valor_2} é par.')
    else:
        print(f'O valor {valor_2} é ímpar.')
else:
    print(f'Não é um número inteiro')
