"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que você digitar: ')
print(numero_str.isdigit())

# numero_float = float(numero_str)
# print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')


# - if está checando uma condição e muda o fluxo do código
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número.')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número.')