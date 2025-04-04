"""
3 - Peça um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.
"""

numero = int(input("Insira um número inteiro: "))

for i in range(1, 11):
     print("{} x {} = {}".format(numero,i,numero*i))
  
