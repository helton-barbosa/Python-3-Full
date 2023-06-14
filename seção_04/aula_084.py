"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis
"""
lista = []
for numero in range(16):
    lista.append(numero)
print(lista)

lista = [
    numero * numero
    for numero in range(16)
]
print(lista)
print()

frutas = [
    fruta.capitalize()
    for fruta in ['abacaxi', 'maçã', 'banana', 'morango', 'sapoti']
]

print(frutas)
print()

# Mapeamento de dados em List Comprehension
produtos = [
    {'nome': 'Produto 1', 'preço': 20},
    {'nome': 'Produto 2', 'preço': 10},
    {'nome': 'Produto 3', 'preço': 21},
    {'nome': 'Produto 3', 'preço': 15},
    {'nome': 'Produto 3', 'preço': 25},
]
novos_produtos = [
    # {**produto, 'preço': produto['preço'] * 1.05}
    {'Nome': produto['nome'], 'Preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]
print(novos_produtos)
print(*novos_produtos, sep='\n')
