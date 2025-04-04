"""
1 - Crie um programa que utilize uma tupla para armazenar as informações de um
produto: nome, preço e quantidade em estoque. Em seguida, exiba os dados do
produto formatados.
"""

produto = ("Notebook", 3500.00, 10)

print(f"Nome: {produto[0]}")
print(f"Preço: R${produto[1]:.2f}")
print(f"Quantidade em Estoque: {produto[2]} unidades")
