"""
1 - Escreva um programa que solicite ao usuário uma lista de números inteiros e
calcule a soma de todos os elementos da lista.
"""

numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
soma = sum(numeros)
print("A soma dos elementos da lista é:", soma)
