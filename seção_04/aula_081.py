"""
Função lambda em Python

A função lambda é uma função como outra qualquer em Python.
Porém, são funções anônimas que contém apenas uma linha.
Ou seja, tudo deve ser contido dentro de uma única expressão.

lista = [
    {'Nome': 'Helton', 'Sobrenome': 'Barbosa'},
    {'Nome': 'Rosilene', 'Sobrenome': 'Xavier'},
    {'Nome': 'João Victor', 'Sobrenome': 'Barbosa'},
    {'Nome': 'Rebecca', 'Sobrenome': 'Ferreira'},
    {'Nome': 'Alailda', 'Sobrenome': 'Santos'},
]
"""

lista_de_numeros_1 = [3, 5, 7, 23, 43, 54, 12, 23, 34, 54, 87, 0, 98, 9, 4]
lista_de_numeros_1.sort()
lista_de_numeros_2 = sorted(lista_de_numeros_1)
print(lista_de_numeros_1)
print(lista_de_numeros_2)

lista = [
    {'Nome': 'Helton', 'Sobrenome': 'Barbosa', 'Idade': 37},
    {'Nome': 'Rosilene', 'Sobrenome': 'Xavier', 'Idade': 40},
    {'Nome': 'João Victor', 'Sobrenome': 'Barbosa', 'Idade': 12},
    {'Nome': 'Rebecca', 'Sobrenome': 'Ferreira', 'Idade': 11},
    {'Nome': 'Alailda', 'Sobrenome': 'Santos', 'Idade': 63},
]


# def ordena(item):
#     return item['Sobrenome']

# lista.sort(key=ordena)

# lista.sort(key=lambda item: item['Idade'])

# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(f'{item}')
    print()


lista_01 = sorted(lista, key=lambda item: item['Nome'])
lista_02 = sorted(lista, key=lambda item: item['Sobrenome'])
lista_03 = sorted(lista, key=lambda item: item['Idade'])

print('Exibir a lista ordenada por Nome')
exibir(lista_01)
print('Exibir a lista ordenada por Sobrenome')
exibir(lista_02)
print('Exibir a lista ordenada por Idade:')
exibir(lista_03)
