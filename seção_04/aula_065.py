"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


def imprimir():
    print('Funções em Python')


def somar(numero_1, numero_2):
    soma = numero_1 + numero_2
    print(f'A soma de {numero_1} + {numero_2} = {soma}')


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


imprimir()
somar(15, 45)
saudacao('Helton Barbosa')
saudacao()
