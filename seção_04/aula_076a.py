# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Helton'
pessoa['sobrenome'] = 'Barbosa'
pessoa['idade'] = 37

print(pessoa)

del pessoa['idade']

print(pessoa)

if pessoa.get('idade') is not None:
    print(pessoa['idade'])
else:
    print(f'Pessoa não tem idade.')
