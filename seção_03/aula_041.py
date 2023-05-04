""" while/else """
string = 'Helton'

i = 0
while i < len(string):
    letra = string[i]
    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('Não enxontrei espaços na string')
print('Fora do while')