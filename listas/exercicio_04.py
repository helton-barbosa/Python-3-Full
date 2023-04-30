"""
Crie uma lista de números inteiros e calcule a média de todos os elementos
"""
lista_numeros = []
soma = 0
media = 0

while True:
    numero = input('Digite um número inteiro ou [sair]: ')

    if numero == 'sair':
        break
    else:
        lista_numeros.append(int(numero))

tamanho_lista = len(lista_numeros)

for number in lista_numeros:
    soma += number

media = soma / tamanho_lista

print(f'Lista original:')
print(lista_numeros)
print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media}')