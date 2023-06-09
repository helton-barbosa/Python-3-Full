# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém, aceitam apenas tipos imutáveis como valor interno.

# Criando um set
# set(iteravel) ou {1, 2, 3}

s1 = set('Helton')
# s1 = {'Helton', 1, 2, 3}
print(s1, type(s1))

# Set são eficientes para remover valores duplicados de iteráveis
# - Eles não tem índexes
# - Eles não garantem ordem
# - Eles são iteráveis (for, in, not in)

s2 = [1, 2, 3, 3, 2, 4, 5, 5, 5, 6]
l1 = set(s2)
print(s2)
print(l1)
print(7 in l1)

# Métodos úteis:
# add, update, clear, dicard

s3 = set()
s3.add('Helton')
s3.add('Barbosa')
s3.add('Santos')
s3.add('Ferreira')
print(s3)
s3.update(('Rosilene', 'Ferreira', 'Xavier', 'Barbosa'))
print(s3)
s3.discard('Santos')
print(s3)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s4 = {0, 1, 2, 3, 4}
s5 = {3, 4, 5, 6, 7}

s6 = s4 | s5
print(f'União {s6}')

s6 = s4 & s5
print(f'Intersecção {s6}')

s6 = s4 - s5
print(f'Diferença {s6}')

s6 = s5 - s4
print(f'Diferença {s6}')

s6 = s4 ^ s5
print(f'Diferença Simétrica {s6}')
