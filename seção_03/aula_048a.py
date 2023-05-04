"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar Ler Alterar Apagar = lista[i] (CRUD)
"""
lista = [10, 20, 3, 40, 50, 60, 70]
print(f'A lista original é {lista}')

numero = lista[2]
print(f'Atribuindo o valor no índice 2 da lista para uma variável -> {numero=}')

lista[2] = 30
print(f'Alterando o valor do índice 2 da lista. Lista atualizada -> {lista}')

del lista[2]
print(f'Deletando o valor do índice 2 da lista. Lista atualizada -> {lista}')

lista.append(80)
print(f'Adicionando um novo valor à lista. Lista atualizada -> {lista}')

valor_removido_1 = lista.pop()
print(f'Removendo o último item [{valor_removido_1}] da lista. Lista atualizada -> {lista}')

valor_removido_2 = lista.pop(2)
print(f'Removendo o item 2 [{valor_removido_2}] da lista. Lista atualizada -> {lista}')