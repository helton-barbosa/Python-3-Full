"""
Faça um programa que pergunte a hora ao usuário, baseando-se no horário descrito,
exiba a saudação apropriada.
Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

linha_completa = 24 * "#"
linha_partes = 4 * "#"

print(f'{linha_completa}')
print(f'{linha_partes} Que Horas São? {linha_partes}')
print(f'{linha_completa}')

hora = input(f'\nDigite a hora atual (hh:mm): ')

somente_hora = int(hora[:-3])
manha = 0 <= somente_hora < 12
tarde = 12 <= somente_hora < 18

if manha:
    print(f'Bom dia! São {hora}')
elif tarde:
    print(f'Boa tarde! São {hora}')
else:
    print(f'Boa noite! São {hora}')