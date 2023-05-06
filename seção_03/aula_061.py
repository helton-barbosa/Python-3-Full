"""
Cálculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 37 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito é 7
"""
cpf = '746.824.890-70'
numeros = []
contador_regressivo_1 = 10
resultado_1 = 0

for i, digito in enumerate(cpf):
    if digito == '.':
        continue
    if digito == '-':
        break

    numeros.append(int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1

for digito in numeros:
    resultado_1 += digito

resultado_1 *= 10
resultado_1 %= 11

primeiro_digito = f'1º dígito é 0.' if resultado_1 > 9 else f'1º dígito é {resultado_1}.'

print(primeiro_digito)
