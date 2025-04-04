"""
2 - Faça um programa que solicite números ao usuário até que ele digite um número negativo.
Quando isso acontecer, o programa deve exibir a soma de todos os números positivos
digitados e encerrar.
"""

positivo = 0
while True:
    x = int(input("Digite um núm positivo: "))
    if x < 0:
        break
    positivo+=x
    print(positivo)
