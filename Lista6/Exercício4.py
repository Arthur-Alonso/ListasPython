"""
4 - Crie uma tupla que armazene o nome de cinco alunos e suas respectivas notas
(ex: ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)). Depois, exiba
apenas os nomes dos alunos e, em seguida, apenas as notas.
"""

alunos_notas = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)

print("Nomes dos alunos:")
for i in range(0, len(alunos_notas), 2):  # Índices pares (0, 2, 4...) são nomes
    print(f"- {alunos_notas[i]}")

print("\nNotas dos alunos:")
for i in range(1, len(alunos_notas), 2):  # Índices ímpares (1, 3, 5...) são notas
    print(f"- {alunos_notas[i]}")
