"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
soma = numero_1 + numero_2
print(soma)
## Uma forma de contornar
print(f'{soma:.2f}')
## Outra forma de contornar
print(round(soma, 2))
## Outra forma
numero_3 = decimal.Decimal('0.5')
numero_4 = decimal.Decimal('0.4')
outra_soma = numero_3 + numero_4
print(outra_soma)
print(round(outra_soma, 2))