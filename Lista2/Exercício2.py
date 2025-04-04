"""
2 - Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
sejam iguais, exiba uma mensagem informando essa condição.
"""

num1 = int(input("Insira um número: "))
num2= int(input("Insira outro número: "))
if num1 > num2:
    print(num1, "é maior")
elif num2 > num1:
    print(num2, "é maior")
elif num1 == num2:
    print(num1, "=", num2)
