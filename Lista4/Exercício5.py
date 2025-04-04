"""
5 - Escreva um programa que peça ao usuário para inserir uma lista de números e um
número específico. O programa deve contar quantas vezes esse número aparece na lista.
"""

numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
numero_especifico = int(input("Digite o número que deseja contar na lista: "))
ocorrencias = numeros.count(numero_especifico)
print(f"O número {numero_especifico} aparece {ocorrencias} vezes na lista.")
