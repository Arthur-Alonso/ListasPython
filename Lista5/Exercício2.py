"""
2 - Crie uma função que receba um número inteiro e retorne True se for primo e False
caso contrário. No programa principal, solicite um número ao usuário e utilize a
função para verificar se ele é primo.
"""

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
numero = int(input("Digite um número para verificar se é primo: "))
if primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
