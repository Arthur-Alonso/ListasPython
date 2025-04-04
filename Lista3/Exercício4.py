"""
4 - Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
ímpares).
"""

num1 = int(input("Insira um numero: "))
num2 = int(input("Insira um numero: "))

for num in range(num1, num2 + 1):
    if num % 2 != 0:
        print(num)
