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
