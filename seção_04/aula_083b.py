def comida_favorita(**kwargs):
    for chave in kwargs:
        print(f'{chave} gosta de {kwargs[chave]}')


comida_favorita(Helton="Caranguejada", Rose="Tacacá")

"""
Ordem dos parâmetros:
    1. Parâmetros definidos def funcao(a, b) 
    2. *args                def funcao(*args)
    3. Parâmetros nomeados  def funcao(cor="Vermelha")
    4. **kwargs             def funcao(**kwargs)
"""