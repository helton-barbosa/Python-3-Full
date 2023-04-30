"""
Crie uma lista de números inteiros e crie uma nova lista com os elementos elevados ao quadrado.
"""
lista_numeros = [7, 5, 6, 4, 9, 3]
lista_quadrado = []

for numero in lista_numeros:
    quadrado = numero * numero
    lista_quadrado.append(quadrado)

print(f'Lista original:')
print(f'{lista_numeros}')
print(f'Lista com números ao quadrado:')
print(f'{lista_quadrado}')