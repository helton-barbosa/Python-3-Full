"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(mensagem, nome):
    return f'{mensagem}, {nome}!'


def executa(funcao, *texto):
    return funcao(*texto)


print(executa(saudacao, 'Bom dia', 'Helton'))
