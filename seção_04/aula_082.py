def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


print(executa(lambda x, y: x + y, 2, 3))

duplica = executa(
    lambda m: lambda n: n * m, 9
)
print(duplica(10))

print(
    executa(
        lambda *args: sum(args), 1, 2, 3, 4, 5
    )
)