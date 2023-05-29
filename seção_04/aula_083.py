# Empacotamento e desempacotamento de dicionários

a, b = 1, 2 # Desempacotando o valor de A e B valor de b nas variáveis A e B
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Helton',
    'sobrenome': 'Barbosa'
}

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
#
# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade': 37,
    'altura': 1.79
}

# Desempacotar dois dicionários em apenas um dicionário
pessoas_completa = {**pessoa, 'cor': 'preta', **dados_pessoa}
print(pessoas_completa)

# args e kwargs
# args (já foi visto nesse curso)
# kwargs - keyword arguments (argumentos nomeados)


def mostra_argumentos_nomeados(*args, **kwargs):
    print(f'Não nomeados: {args}')
    print(f'Nomeados:')
    for chave, valor in kwargs.items():
        print(chave, valor)


mostra_argumentos_nomeados(10, 20, 30, nome='Rose', sei_la=123)
mostra_argumentos_nomeados(**pessoas_completa)
