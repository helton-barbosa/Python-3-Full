"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'Python é uma linguagem de programação, uma entre várias existentes.'
lista_palavras = frase.split()
lista_frases = frase.split(', ')
print(lista_palavras)
print(lista_frases)

frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)