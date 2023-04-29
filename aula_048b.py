"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final da lista. Qualquer dado.
    insert - Adiciona um item na lista no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    Extend - Estende a lista
    + - Concatena as listas
Create  Read    Update  Delete
Criar   Ler     Alterar Apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
print(f'Lista original -> {lista}')

append_01 = 'Python'
append_02 = False
lista.append(append_01)
lista.append(append_02)
print(f'Adicionando {append_01} e {append_02} à lista. Lista atualizada -> {lista}')

pop_01 = lista.pop(5)
print(f'Removendo {pop_01} da lista. Lista atualizada -> {lista}')

del lista[-1]
print(f'Deletando o último item da lista. Lista atualizada -> {lista}')

indice_add = 0
item_add = 'Flamengo'
lista.insert(indice_add, item_add)
print(f'Adicionando {item_add} no índice {indice_add} da lista. Lista atualizada-> {lista}')