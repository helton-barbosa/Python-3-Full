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

lista_a = [1, 'Helton', 3]
lista_b = [4, 'Barbosa', 6]
lista_c = lista_a + lista_b
print(lista_c)

lista_d = lista_a.extend(lista_b)
print(lista_a)