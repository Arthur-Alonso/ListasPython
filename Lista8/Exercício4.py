"""
4 - Crie uma lista com cinco números e permita que o usuário informe um índice para
acessar um valor da lista. Utilize tratamento de exceções para evitar erros caso o
usuário digite um índice inválido.
"""

def acesso_lista():
    lista = [1, 2, 3, 4, 5]
    try:
        indice = int(input("Digite o índice (0 a 4) para acessar o valor da lista: "))
        print(f"Valor no índice {indice}: {lista[indice]}")
    except IndexError:
        print("Erro: Índice inválido. A lista possui índices de 0 a 4.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")

acesso_lista()
