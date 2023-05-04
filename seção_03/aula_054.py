"""
Faça uma lista de compras utilizando listas
O usuário deve ter a possibilidade de:
- inserir
- apagar
- listar
Não permita que o programa quebre com erros de índices inexistentes na lista
"""
import os

lista_compras = []
item = ''
indice = 0

while True:
    opcao = input('Selecione uma opção\n[i]nserir - [a]pagar - [l]istar - [s]air: ')

    if opcao == 'i':
        item = input('Digite o item para adicionar na lista: ')
        lista_compras.append(item)
    elif opcao == 'a':
        try:
            indice = int(input('Escolha o índice para apagar na lista: '))
            lista_compras.pop(indice)
        except IndexError:
            print(f'O índice {indice} não existe na lista.')
    elif opcao == 'l':
        os.system('clear')
        for indice, produto in enumerate(lista_compras):
            print(indice, produto)
    elif opcao == 's':
        print('Saindo...')
        os.system('sleep 1')
        break
    else:
        print(f'Opção inexistente')