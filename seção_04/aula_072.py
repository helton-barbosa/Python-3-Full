# Exercício com funções

"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que retorna se um número é Par ou Ímpar
"""


def multiplicar(*args):
    produto = 1
    for numeros in args:
        produto *= numeros

    return produto


def par_ou_impar(numero):
    if numero == 0:
        return 'Número Nulo'
    elif numero % 2 == 0:
        return 'Número Par'
    else:
        return 'Número Ímpar'


resultado_multiplicacao = multiplicar(5, 5)
print(resultado_multiplicacao)

resultado_par_ou_impar = par_ou_impar(2)
print(resultado_par_ou_impar)
