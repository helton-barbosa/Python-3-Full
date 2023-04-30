"""
Crie uma lista de nomes de pessoas e ordene-a em ordem alfabética
"""

lista_nomes = []

while True:
    nome = input('Digite um nome ou 1 para sair: ')
    if nome == '1':
        break
    else:
        lista_nomes.append(nome)

print(f'Lista de nomes original:')
print(lista_nomes)
print(f'Lista de nome em ordem alfabética:')
lista_nomes.sort(reverse=False)
print(lista_nomes)