"""
4 - Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
por hora. O programa deve calcular e exibir o salário total do mês.
"""

horas_trabalhadas = float(input("Digite o numero de horas trabalhadas: "))
valor_por_hora = float(input("Insira o valor da hora: "))

salario = horas_trabalhadas * valor_por_hora
print(salario)
