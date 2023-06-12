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
