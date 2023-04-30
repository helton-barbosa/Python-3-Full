"""
Crie uma lista de palavras e ordene-as em ordem crescente de tamanho (número de caracteres)
"""
lista_palavras = []

while True:
    palavra = input('Digite uma palavra ou [1] para sair: ')

    if palavra == '1':
        break
    else:
        lista_palavras.append(palavra)

print(f'Lista de palavras original:')
print(lista_palavras)
lista_palavras.sort(key=len)
print(f'Lista de palavras em ordem crescente de tamanho:')
print(lista_palavras)