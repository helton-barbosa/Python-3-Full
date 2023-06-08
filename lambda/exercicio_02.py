"""
Escreva uma função lambda que verifique se um número é par
"""


def executa(funcao, *args):
    return funcao(*args)


numero = int(input('Digite um número: '))
resultado = executa(lambda num: f"{numero} é par" if (num % 2 == 0) else f"{numero} é ímpar", numero)
print(resultado)
