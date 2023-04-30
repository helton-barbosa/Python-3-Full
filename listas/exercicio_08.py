"""
Crie uma lista de strings e crie uma nova lista com apenas strings que começam com a letra 'a'.
"""
lista_a = []
lista_strings = ['arara', 'aracaju', 'parede', 'futebol', 'comida', 'faca', 'azul', 'estado', 'argentina', 'água', 'pequi', 'aranha']

for palavra in lista_strings:
    if palavra[0] == 'a' or palavra[0] == 'á':
        lista_a.append(palavra)

print(f'Lista original:')
print(f'{lista_strings}')
print(f'Lista de strings apenas com a letra inicial "a":')
print(lista_a)