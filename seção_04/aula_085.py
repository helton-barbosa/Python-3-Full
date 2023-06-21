lista = []

# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

"""
O código comentado acima, é o mesmo que abaixo
"""
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)
