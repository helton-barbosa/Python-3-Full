"""
Introdução à List Comprehension em Python
List Comprehension é uma forma rápida para criar listas a partir de iteráveis
"""
lista = []
for numero in range(21):
    lista.append(numero)
# print(lista)

lista = [
    numero * numero
    for numero in range(16)
]
print(lista)
print()

# Mapeamento de dados em list comprehension
produtos = [
    {'Nome': 'produto_1', 'Preço': 20, },
    {'Nome': 'produto_2', 'Preço': 10, },
    {'Nome': 'produto_3', 'Preço': 30, },
]
novos_produtos = [
    produtos
    for produto in produtos
]
print(*novos_produtos, sep='\n')