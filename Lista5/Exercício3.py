"""
3 - Crie uma função que receba uma lista de números e retorne a média dos valores.
No programa principal, peça ao usuário para inserir os números e exiba a média
utilizando a função criada.
"""

def media(lista):
    return sum(lista) / len(lista)
numeros = list(map(int, input("Digite números separados por espaço: ").split()))
media = media(numeros)
print(f"A média dos números inseridos é: {media}")
