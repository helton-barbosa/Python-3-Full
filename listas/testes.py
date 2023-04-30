lista = [10, 20, 30, 40, 50, 60]
print(lista)

lista.append('Arara')
lista.append(10)
print(lista)

print(f'{lista.count(10)}')

frutas = ['Laranja', 'Ingá', 'Uva', 'Limão', 'Caju', 'Manga']

# try:
#     fruta = input('Qual fruta está pesquisando? ')
#     indice_procurado = frutas.index(fruta)
#     print(f'A fruta {fruta} está no índice {indice_procurado}')
#     print(frutas)
# except ValueError:
#     print(f'A fruta {fruta} não está na lista.')
#     print(frutas)

frutas.insert(len(frutas), 'Azeitona')
frutas.insert(len(frutas), 'Pitomba')
frutas.insert(len(frutas), 'Cajá')
print(frutas)

fruta_removida = frutas.pop()
print(f'Removida a fruta {fruta_removida} da lista.')
print(frutas)

try:
    fruta_a_remover = input('Digite fruta a remover: ')
    print(f'A fruta {fruta_a_remover} está no índice {frutas.index(fruta_a_remover)}')
    frutas.remove(fruta_a_remover)
    print(f'Lista atualizada. -> {frutas}')
except ValueError:
    print(f'A fruta {fruta_a_remover} não está na lista.')