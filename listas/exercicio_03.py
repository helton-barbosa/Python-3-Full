"""
Crie uma lista de números inteiros e calcula a soma de todos os elementos
"""
lista_numeros = []
soma = 0

while True:
    numero = input('Digite um número inteiro ou [sair]: ')

    if numero == 'sair':
        break
    else:
        lista_numeros.append(int(numero))


for number in lista_numeros:
    soma += number

print(f'Lista: {lista_numeros} Soma: {soma}')