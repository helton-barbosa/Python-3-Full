"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)

texto = 'Helton'.__iter__()
print(texto)
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

texto1 = ('Rose')
iterador = iter(texto1)
print(texto1)
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break