"""
3 - Crie um programa que receba três números do usuário e calcule a média aritmética deles.
"""

numeros = []
for i in range (0,3):
    numeros.append(float(input("Insira 3 números: ")))
soma = sum(numeros)
media = soma / 3
print(media)
