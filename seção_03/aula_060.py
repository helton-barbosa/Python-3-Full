"""
Operação ternária (condicional em uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = True
variavel = 'Verdadeiro' if condicao else 'Falso'
print(variavel)

digito = 10
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')
