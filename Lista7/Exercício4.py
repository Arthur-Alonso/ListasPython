"""
4 - Peça ao usuário para inserir uma frase. Utilize um dicionário para armazenar a
contagem de palavras, ou seja, a chave será a palavra e o valor será o número de
vezes que ela aparece na frase. Exiba o dicionário ao final.
"""

frase = input("Digite uma frase: ").strip().lower()

palavras = frase.split()

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print("\nContagem de palavras na frase:")
for palavra, quantidade in contagem_palavras.items():
    print(f"'{palavra}': {quantidade}")

