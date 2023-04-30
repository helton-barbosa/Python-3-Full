"""
Crie uma lista de números inteiros e uma variável maior com valor zero. Percorra a lista e atribua o maior valor encontrado à variável maior.
"""

lista_inteiros = []

while True:
    numero = input('Digite um número inteiro ou [sair]: ')

    if numero == 'sair':
        break
    else:
        lista_inteiros.append(int(numero))

maior = 0

for number in lista_inteiros:
    if number > maior:
        maior = number

print(f'Lista original:')
print(lista_inteiros)
print(f'O maior valor dessa lista é {maior}')