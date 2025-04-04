"""
5 - Peça ao usuário três números representando os lados de um triângulo. O programa deve
verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
sempre maior que o terceiro).
"""

lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))

if (lado1 + lado2) > lado3:
    print('triângulo válido')
elif (lado1 + lado3) > lado2:
    print('triângulo válido')
elif (lado2 + lado3) > lado1:
    print('triângulo válido')
else:
    print('triângulo inválido')
