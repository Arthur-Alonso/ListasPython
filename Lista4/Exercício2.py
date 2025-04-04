"""
2 - Escreva um programa que leia uma lista de números digitados pelo usuário e
determine o maior e o menor número presentes na lista.
"""

numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
maior = max(numeros)
menor = min(numeros)
print("O maior número é:", maior)
print("O menor número é:", menor)
