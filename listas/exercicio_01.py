"""
Crie uma lista de números inteiros e ordene-a em ordem crescente.
"""
lista_numeros = []

while True:
    numero = input('Digite um número inteiro ou [sair]: ')

    if numero == 'sair':
        break
    else:
        lista_numeros.append(int(numero))

print(f'Essa é a lista criada original -> {lista_numeros}')
lista_numeros.sort(reverse=False)
print(f'Essa é a lista ordenada -> {lista_numeros}')