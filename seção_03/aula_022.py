# Operadores Lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy os seguintes valores:
# 0 0.0 '' False, [], (), {}, set()
# Também existe o tipo None que é usado para representar um não valor

# entrada = input('[E]ntrar - [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entrar')
# else:
#    print('Sair')

# Avaliação de curto circuito (serve para economizar os recursos)
avalia = 0 or False or 0.0 or 'Deu certo!' or True
print(avalia)
# A avaliação foi verificada e quando chegou no primeiro Truthy ('Deu certo!'),
# o código não prossegue, para nesse primeiro valor True.

avalia_senha = input('Senha: ') or 'Sem senha.'
print(avalia_senha)