"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return 10, 20
    return x + y


# variavel = print('O print é uma função que retorna None')
# print(variavel)

# variavel1 = soma(1, 2)
# variavel2 = int('1')
# print(variavel1)
# print(variavel2)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma1 + soma2)
print(soma(11, 5))
