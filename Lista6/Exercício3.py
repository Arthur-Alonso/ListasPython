"""
3 - Crie uma tupla contendo as cores do arco-íris em ordem. Depois, permita que o
usuário informe um número de 1 a 7 e exiba a cor correspondente.
"""

cores_arco_iris = (
    "Vermelho",
    "Laranja",
    "Amarelo",
    "Verde",
    "Azul",
    "Anil",
    "Violeta"
)

numero = int(input("Digite um número de 1 a 7 para ver a cor correspondente do arco-íris: "))

if 1 <= numero <= 7:
    cor_escolhida = cores_arco_iris[numero - 1]  # Ajuste do índice (tuplas começam em 0)
    print(f"A cor na posição {numero} é {cor_escolhida}.")
else:
    print("Número inválido! Por favor, digite um número entre 1 e 7.")
