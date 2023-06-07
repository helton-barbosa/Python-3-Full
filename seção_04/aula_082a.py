def executa(funcao, *args):
    return funcao(*args)


multiplicar = executa(lambda x, y: x * y, 5, 5)
somar_1 = executa(lambda x, y, z: x + y + z, 123, 456, 789)
print(multiplicar)
print(somar_1)

