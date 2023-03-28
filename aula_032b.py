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

entrada = input(f'\nDigite a hora atual (apenas a hora): ')

try:
    hora = int(entrada)
    hora_valida = 0 <= hora < 24 

    manha = 0 <= hora < 12
    tarde = 12 <= hora < 18

    if hora_valida:
        if manha:
            print(f'Bom dia!')
        elif tarde:
            print(f'Boa tarde!')
        else:
            print(f'Boa noite!')
    else:
        print(f'A hora {hora} não é válida!')
except:
    print(f'Digite apenas horas válidas.')