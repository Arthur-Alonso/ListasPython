"""
2 - Solicite ao usuário quatro números inteiros e armazene-os em uma tupla. Em
seguida, exiba:
• Quantas vezes o número 9 apareceu na tupla.
• Em que posição foi digitado o primeiro número 3 (caso exista).
• Os números pares contidos na tupla.
"""

numeros = (
    int(input("Digite o 1º número inteiro: ")),
    int(input("Digite o 2º número inteiro: ")),
    int(input("Digite o 3º número inteiro: ")),
    int(input("Digite o 4º número inteiro: "))
)

print(f"\nNúmeros digitados: {numeros}")

quant_nove = numeros.count(9)
print(f"O número 9 apareceu {quant_nove} vez(es).")

if 3 in numeros:
    posicao_tres = numeros.index(3) + 1 
    print(f"O primeiro número 3 foi digitado na {posicao_tres} posição.")
else:
    print("O número 3 não foi digitado.")

pares = [num for num in numeros if num % 2 == 0]
if pares:
    print(f"Números pares digitados: {pares}")
else:
    print("Nenhum número par foi digitado.")
