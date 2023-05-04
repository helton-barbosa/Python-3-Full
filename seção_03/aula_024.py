# Operadores in e not in
# in - está entre
# not in - não está entre
# Strings são iteráveis
#  0 1 2 3 4 5
#  H e l t o n
# -6-5-4-3-2-1

# nome = 'Helton'
# print(nome[2])
# print(nome[4])

# print('to' in nome)
# print('ze' not in nome)
# print(10 * '-')

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
   print(f'A expressão "{encontrar}" está em "{nome}"')
else:
   print(f'A expressão "{encontrar}" não está em "{nome}"')
