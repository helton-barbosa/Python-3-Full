"""
Exercício:
Interando strings com while
"""

# *H*e*l*t*o*n

nome = input('Digite o nome que deseja iterar: ')
tamanho_nome = len(nome)
iterador = 0
novo_nome = ''

while iterador < tamanho_nome:
    novo_nome += '*' + nome[iterador]
    iterador += 1

print(f'O nome modificado ficará assim: {novo_nome}')