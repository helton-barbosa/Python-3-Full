"""
Crie uma lista de números inteiros e crie uma nova lista com apenas os elementos pares
"""
numeros_pares = []
numeros_inteiros = []

while True:
    numero = input('Digite um número inteiro ou [sair]: ')

    if numero == 'sair':
        break
    else:
        numeros_inteiros.append(int(numero))

for number in numeros_inteiros:
    if number % 2 == 0:
        numeros_pares.append(number)

print(f'Números inteiros:')
print(numeros_inteiros)
print(f'Números pares:')
print(numeros_pares)