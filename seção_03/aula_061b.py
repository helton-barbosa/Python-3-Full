"""
Cálculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Exemplo: 746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0  7
    77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 10
3630 % 11 0
    Se o resultado anterior for maior que 9:
        resultado é 0
    Contrário disso:
        resultado é o valor da conta
"""

cpf = '181.086.020-25'
numeros = []
contador_regressivo_2 = 11
resultado_2 = 0

for i, digito in enumerate(cpf):
    if digito == '.' or digito == '-':
        continue

    numeros.append(int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1

    if i == 12:
        break

for digito in numeros:
    resultado_2 += digito

resultado_2 *= 10
resultado_2 %= 11

primeiro_digito = f'2º dígito é 0.' if resultado_2 > 9 else f'2º dígito é {resultado_2}.'

print(primeiro_digito)
