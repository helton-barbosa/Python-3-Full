# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy os seguintes valores:
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar - [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
   print('Entrar')
else:
   print('Sair')

# Avaliação de curto circuito (serve para economizar os recursos)
print(True and False and True)
# A avaliação foi verificada e quando chegou no primeiro False,
# o código não prossegue, para nesse primeiro valor False