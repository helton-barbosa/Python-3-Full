cpf = '746.824.890-70'
numeros_1 = []
numeros_2 = []
pri_digito = int(cpf[-2])
seg_digito = int(cpf[-1])
contador_regressivo_1 = 10
contador_regressivo_2 = 11
resultado_1 = 0
resultado_2 = 0

for i, digito in enumerate(cpf):
    if digito == '.':
        continue
    if digito == '-':
        break

    numeros_1.append(int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1

for digito in numeros_1:
    resultado_1 += digito

resultado_1 *= 10
resultado_1 %= 11

primeiro_digito = f'1º dígito é 0.' if resultado_1 > 9 else f'1º dígito é {resultado_1}.'

for i, digito in enumerate(cpf):
    if digito == '.' or digito == '-':
        continue

    numeros_2.append(int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1

    if i == 12:
        break

for digito in numeros_2:
    resultado_2 += digito

resultado_2 *= 10
resultado_2 %= 11

segundo_digito = f'2º dígito é 0.' if resultado_2 > 9 else f'2º dígito é {resultado_2}.'

if pri_digito == resultado_1 and seg_digito == resultado_2:
    print(f'O cpf {cpf} é válido!')
else:
    print(f'O cpf {cpf} não é válido.')
