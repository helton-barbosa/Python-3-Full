"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
print(falar_bom_dia)
print(falar_bom_dia('Helton'))

falar_boa_noite = criar_saudacao('Boa noite')
print(falar_boa_noite)
print(falar_boa_noite('Helton'))

nomes = 'Helton', 'Rose', 'João Victor', 'Rebecca'

for i in nomes:
    print(falar_boa_noite(i))
