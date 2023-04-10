"""
Repetições
while(enquanto)
Executa uma ação enquanto a condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 30:
    contador += 1
    if contador % 2 == 0:
        print(f'O número {contador} é PAR.')
    else:
        print('Número ÍMPAR.')
        continue