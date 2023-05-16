"""
Exercícios
Crie funções que dupliquem, tripliquem e quadrupliquem o número recebido como parâmetro
"""


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


number = 100

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(f'Número {number} duplicado é {duplicar(number)}')
print(f'Número {number} triplicado é {triplicar(number)}')
print(f'Número {number} quadruplicado é {quadruplicar(number)}')
