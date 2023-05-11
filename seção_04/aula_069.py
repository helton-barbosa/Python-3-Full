"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existem o escopo global e local
O escopo global é o escopo onde todo o código é alcançável
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados

Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma do escopo interno.
"""

x = 1


def escopo():
    # global x
    x = 10
    print(x)

    def outra_funcao():
        # global x
        x = 30
        y = 20
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
