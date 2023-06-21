"""
Dictionary Comprehension e Set Comprehension
"""
produto = {
    'Nome': 'Impressora HP Tank Wireless',
    'Preço': 1200.00,
    'Quantidade': 15,
    'Categoria': 'Escritório'
}

for chave, valor in produto.items():
    print(chave, valor)
print()

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
    if chave != 'Categoria'
}

print(dc)
