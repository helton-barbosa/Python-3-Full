"""
List COmprehension é uma forma concisa de criar listas em Python. É uma técnica poderosa e elegante que permite criar
listas de forma eficiente usando uma sintaxe compacta. EM vez de usar loops tradicionais, pode-se usar List
Comprehension para realizar operações em elementos de uma lista ou iteráveis e então criar uma nova lista com os
resultados
A seguir, uma forma tradicional de usar a List Comprehension:
    nova_lista = [expressão for item in iterável if condição]
Mas também podemos usar da seguinte forma:
    nova_lista = [
        expressão
        for item in iterável
        if condição
    ]
"""
# Exemplo 1: Criando uma lista de números elevados ao quadrado.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_ao_quadrado = [
    num ** 2
    for num in numeros
]
print('Exemplo 1: Criando uma lista de números elevados ao quadrado.')
print(f'{numeros_ao_quadrado}\n')

# Exemplo 2: Filtrando números pares de uma lista.
numeros = range(25)
numeros_impares = [
    x
    for x in numeros
    if x % 2 == 0
]
print('Exemplo 2: Filtrando números pares de uma lista.')
print(f'{numeros_impares}\n')

# Exemplo 3: Criando uma lista de strings em maiúsculas.
frutas = ('banana', 'kiwi', 'laranja', 'abacate', 'abacaxi', 'tangerina')
lista_frutas = [
    palavra.upper()
    for palavra in frutas
]
print('Exemplo 3: Criando uma lista de strings em maiúsculas.')
print(f'{lista_frutas}\n')