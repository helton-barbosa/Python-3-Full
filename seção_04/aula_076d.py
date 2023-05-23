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
    'ano_nascimento': 1985,
    'cidade_nascimento': 'Aracaju',
    'info_adicionais': 'Nada de novo'
}

# get
print(pessoa.get('nome'))
print(pessoa.get('idade', 'Idade não existe'))

# pop
nome = pessoa.pop('nome')
print(nome)
print(pessoa)

print(f'\n')
# popitem
ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

print(f'\n')
# update
pessoa.update({
    'nome': 'Rebecca',
    'idade': 11,
})
pessoa.update(ano_nascimento=2012)
print(pessoa)
