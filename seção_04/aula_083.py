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

# Desempacotar dois dicionários e empacotar em apenas um dicionário
pessoas_completa = {**pessoa, 'cor': 'Preta', **dados_pessoa}
print(pessoas_completa)
print()

# args e kwargs
# args (já foi visto nesse curso)
# kwargs - keyword arguments (argumentos nomeados)


def mostra_argumentos_nomeados(*args, **kwargs):
    print(f'Não nomeados: {args}')
    print(f'Nomeados:')
    for chave, valor in kwargs.items():
        print(chave, valor)


mostra_argumentos_nomeados(10, 20, 30, nome='Rose', sei_la=123)
print()
mostra_argumentos_nomeados(**pessoas_completa)
print()


def soma(n1, n2, n3):
    return n1 + n2 + n3


print(soma(10, 12, 14))


def soma_args(*args):
    # total = 0
    # for i in args:
    #     total += i
    # ou podemos usar uma função sum()
    return sum(args)


print(soma_args(15, 20, 35, 45))


def mostrar(*args):
    print(args)


mostrar(10, 20, 30, 40)