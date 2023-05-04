"""
Exercício:
Interando strings com while
"""

# *H*e*l*t*o*n

nome = input('Digite o nome que deseja modificar: ')
tamanho_nome = len(nome)
indice = 0
novo_nome = ''

while indice < tamanho_nome:
    novo_nome += f'*{nome[indice]}'
    indice += 1

print(f'O nome modificado ficará assim: {novo_nome}')