"""
5 - Escreva um programa que peça ao usuário um número N e exiba os N primeiros termos da
Sequência de Fibonacci.
Obs: A sequência de Fibonacci começa com 0 e 1, e cada termo seguinte é a soma dos dois
anteriores:
"""

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Digite o número de termos da sequência de Fibonacci: "))

print(fibonacci(n))
