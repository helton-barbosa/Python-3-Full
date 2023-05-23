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
pessoa = {
    'nome': 'Helton',
    'sobrenome': 'Barbosa',
    'sobrenome': 'Barbosa',
}  # caso existam chaves duplicadas, o python só considera o último

# len
print(pessoa.__len__())
print(len(pessoa))

# keys
print(pessoa.keys())
# posso transformar o resultado de uma keys em tupla ou lista
print(list(pessoa.keys()))
print(tuple(pessoa.keys()))
# posso utilizar o for para percorrer as chaves
for chave in pessoa.keys():
    print(chave)

# values
print(pessoa.values())
# posso utilizar o for para percorrer os valores
for valor in pessoa.values():
    print(valor)

# items
print(pessoa.items())
# posso utilizar o for para percorrer os items
for chave, valor in pessoa.items():
    print(f'Chave: {chave} - Valor: {valor}')

# setdefault
pessoa.setdefault('idade', 37)
print(pessoa['idade'])
