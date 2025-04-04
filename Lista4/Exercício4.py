"""
4 - Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem
inversa.
"""

palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
palavras_invertidas = palavras[::-1]
print("Lista invertida:", palavras_invertidas)
