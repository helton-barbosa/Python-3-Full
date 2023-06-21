"""
# isinstance serve para verificar se o objeto é de um determinado tipo
"""

lista = ['a', 'h', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'Nome': 'Helton'}]

for item in lista:
    if isinstance(item, set):
        item.add(7)
        print(f'Conjuntos SET\n{item}')
    elif isinstance(item, str):
        print(f'String\n{item.upper()}')

    elif isinstance(item, (int, float)):
        print(f'Numéricos (int ou float)\n{item * 2.5}')
    else:
        print(f'Outros Tipos\n{item}')
