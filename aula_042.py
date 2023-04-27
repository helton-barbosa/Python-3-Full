frase = 'Helton Barbosa'
tamanho_frase = len(frase)
i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ''
while i < tamanho_frase:
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_mais_vezes < qtd_atual:
        qtd_mais_vezes = qtd_atual
        letra_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_mais_vezes}" que apareceu {qtd_mais_vezes}x')