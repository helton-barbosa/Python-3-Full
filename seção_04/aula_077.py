# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '4', '3', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertou = 0

for id, questao in enumerate(perguntas):
    print(f"Pergunta nº {id + 1}: {questao['Pergunta']}\n")
    print('Opções:')

    if id == 0:
        for item, pergunta in enumerate(perguntas[id]['Opções']):
            print(f"{item}) {pergunta}")
        resposta_1 = int(input('Escolha uma opção: '))
        if perguntas[id]['Resposta'] == perguntas[id]['Opções'][resposta_1]:
            print('Acertou\n')
            acertou += 1
            continue
        else:
            print('Errou\n')
            continue
    elif id == 1:
        for item, pergunta in enumerate(perguntas[id]['Opções']):
            print(f"{item}) {pergunta}")
        resposta_1 = int(input('Escolha uma opção: '))
        if perguntas[id]['Resposta'] == perguntas[id]['Opções'][resposta_1]:
            print('Acertou\n')
            acertou += 1
            continue
        else:
            print('Errou\n')
            continue
    elif id == 2:
        for item, pergunta in enumerate(perguntas[id]['Opções']):
            print(f"{item}) {pergunta}")
        resposta_1 = int(input('Escolha uma opção: '))
        if perguntas[id]['Resposta'] == perguntas[id]['Opções'][resposta_1]:
            print('Acertou\n')
            acertou += 1
            continue
        else:
            print('Errou\n')
            continue

print(f'Você acertou {acertou} de {len(perguntas[0])}.')
