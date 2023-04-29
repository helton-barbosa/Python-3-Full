"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Helton', 'Rose', True, 100]
lista_b = lista_a.copy()

lista_a[0] = 'Casa'
print(f'Lista A {lista_a}')
print(f'Lista B {lista_b}')