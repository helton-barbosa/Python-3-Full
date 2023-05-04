"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"
Se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal"
Se o nome tiver mais que 6 letras, escreva "Seu nome é muito grande".
"""
linha_completa = 25 * "#"
linha_partes = 4 * "#"

print(f'{linha_completa}')
print(f'{linha_partes} Tamanho do Nome {linha_partes}')
print(f'{linha_completa}')

nome = input("\nDigite o seu primeiro nome: ")

nome_curto = len(nome) <= 4
nome_medio = 5 <= len(nome) <= 6

if nome_curto:
    print(f'O nome {nome} é curto.')
elif nome_medio:
    print(f'O nome {nome} é normal.')
else:
    print(f'O nome {nome} é muito grande.')
