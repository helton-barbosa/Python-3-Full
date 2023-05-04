"""
Introdução ao desempacotamento + tuples (tuplas)
"""
nomes = ['Helton', 'Rose', 'João Victor', 'Rebecca']
nome_fulano, nome_ciclano, nome_beltrano, outro_nome = nomes
print(nome_fulano)
print(nome_ciclano)
print(nome_beltrano)
print(outro_nome)
print('\n')
capixaba, carioca, paulista, mineiro = ['Espírito Santo', 'Rio de Janeiro', 'São Paulo', 'Minas Gerais']
print(capixaba)
print(carioca)
print(paulista)
print(mineiro)
print('\n')

_, cor2, *_ = ['Amarelo', 'Azul', 'Verde', 'Preto']
print(cor2)