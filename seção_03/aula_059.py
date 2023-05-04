"""
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = ('Python', 'é', 'legal')

clubes = [
    ['Flamengo', 'Botafogo', 'Fluminense', 'Vasco da Gama', ],
    ['Palmeiras', 'Santos', 'Corinthians', 'São Paulo', ],
    ['Cruzeiro', 'Atlético - MG', 'América - MG', ],
    ['Palmas', 'Tocantinópolis', 'Interporto', 'Capital', ],
]

for item in lista:
    print(item, end=' ')

# Podemos desempacotar desta forma...
print('\n')

for item in string:
    print(item, end=' ')

print('\n')

for item in tupla:
    print(item, end=' ')

print('\n')

# Mas também podemos desempacotar dessa outra forma...
print(*string)
print(*lista)
print(*tupla)

print(*clubes, sep='\n')
