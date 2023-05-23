"""
Métodos úteis dos Dicionários em Python

len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""
import copy

# Exemplos de cópia rasa (shallow copy)
dicionario_1 = {
    'chave_1': 1,
    'chave_2': 2,
    'lista': [0, 1, 2, 3]
}

dicionario_2 = dicionario_1.copy()

dicionario_2['chave_1'] = 10
dicionario_2['lista'][1] = 1995

print(dicionario_1)
print(dicionario_2)

# Exemplos de cópia profunda (deep copy)
dicionario_3 = {
    'chave_1': 1,
    'chave_2': 2,
    'lista': [0, 1, 2, 3]
}

dicionario_4 = copy.deepcopy(dicionario_3)

dicionario_4['chave_1'] = 10
dicionario_4['lista'][1] = 2023
print('\n')
print(dicionario_3)
print(dicionario_4)
