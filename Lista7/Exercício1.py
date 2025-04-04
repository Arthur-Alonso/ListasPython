"""
1 - Crie um programa que permita cadastrar alunos em um dicionário. O programa
deve solicitar o nome e a nota do aluno e armazená-los como chave e valor no
dicionário. Após a inserção de pelo menos 3 alunos, exiba a lista de alunos e suas
respectivas notas.
"""

alunos = {}

print("=== Cadastro de Alunos ===")

while len(alunos) < 3:
    nome = input("Digite o nome do aluno: ").strip()
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota
    print(f"Aluno {nome} cadastrado com nota {nota}.\n")

while True:
    continuar = input("Deseja cadastrar mais um aluno? (s/n): ").strip().lower()
    if continuar == 's':
        nome = input("Digite o nome do aluno: ").strip()
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota
        print(f"Aluno {nome} cadastrado com nota {nota}.\n")
    else:
        break

print("\n=== Lista de Alunos Cadastrados ===")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")

