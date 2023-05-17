"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor".

Chaves podem ser consideradas como o "índice" que vimos na lista e
podem ser de tipos imutáveis (str, int, float, bool, tuple e etc).

O valor pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list
"""

pessoa = {
    'nome': 'Helton',
    'sobrenome': 'Barbosa',
    'idade': 37,
    'altura': 1.79,
    'endereços': [
        {'rua': 'Logo ali', 'número': 123},
        {'rua': 'Mais na frente', 'número': 456},
    ]
}
# print(pessoa, type(pessoa))

# clubes = dict(time='Flamengo', estado='Rio de Janeiro')
# print(clubes, type(clubes))

# print(pessoa['endereços'][0]['rua'])
for chave in pessoa:
    print(chave, pessoa[chave])
