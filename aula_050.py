"""
Exercício
Exiba os índices da lista
"""

lista = ['Manga', 'Acerola', 'Maracujá', 'Azeitona']

# # Solução 1
# indice = 0
# for item in lista:
#     print(f'No índice {indice} há o item "{item}"')
#     indice += 1

# Solução 2
indices = range(len(lista))
for indice in indices:
    print(f'No índice {indice} há o item "{lista[indice]}"')
