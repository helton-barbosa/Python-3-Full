"""
Crie uma lista de números inteiros e crie uma nova lista com os elementos que são divisíveis por 3.
"""
lista_div_tres = []
lista_numeros = list(range(1, 51))

for numero in lista_numeros:
    if numero % 3 == 0:
        lista_div_tres.append(numero)

print(lista_numeros)
print(f'Números divisíveis por 3:')
print(f'{lista_div_tres}')