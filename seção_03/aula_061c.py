import re

cpf = '062.922.131-61'
numeros_1 = []
numeros_2 = []
pri_digito = int(cpf[-2])
seg_digito = int(cpf[-1])
contador_regressivo_1 = 10
contador_regressivo_2 = 11
resultado_1 = 0
resultado_2 = 0

cpf_limpo = re.sub(
    r'[^0-9]',
    '',
    cpf
)

for digito in cpf_limpo:
    numeros_1.append(int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1

    if contador_regressivo_1 == 1:
        break

for digito in numeros_1:
    resultado_1 += digito

resultado_1 *= 10
resultado_1 %= 11

if resultado_1 > 9:
    resultado_1 = 0
else:
    resultado_1 = resultado_1

for digito in cpf_limpo:
    numeros_2.append(int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1

    if contador_regressivo_2 == 1:
        break

for digito in numeros_2:
    resultado_2 += digito

resultado_2 *= 10
resultado_2 %= 11

if resultado_2 > 9:
    resultado_2 = 0
else:
    resultado_2 = resultado_2

if pri_digito == resultado_1 and seg_digito == resultado_2:
    print(f'O cpf {cpf} é válido!')
else:
    print(f'O cpf {cpf} não é válido.')
