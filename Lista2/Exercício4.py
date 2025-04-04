"""
4 - Elabore um programa que solicite duas notas ao usuário e calcule a média. Em seguida,
informe se o aluno foi:
• Aprovado (média maior ou igual a 7)
• Recuperação (média entre 5 e 6.9)
• Reprovado (média abaixo de 5)
"""

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2
if media >= 7:
    print('Aprovado')
if 5 < media < 6.7:
    print("Recuperação")
if media < 5:
    print('Reprovado')
