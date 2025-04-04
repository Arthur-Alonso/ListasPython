"""
5 - Crie um dicionário onde as chaves representem códigos de produtos e os valores
sejam tuplas contendo o nome do produto e seu preço. Permita que o usuário
informe um código para buscar o nome e o preço do produto correspondente.
"""

catalogo = {
    01: ("Tablet", 1800.00),
    02: ("Smartwatch", 1200.00),
    03: ("Mouse", 80.00),
    04: ("Impressora", 950.00),
    05: ("Caixa de Som", 300.00)
}

print("Produtos")
print("Códigos disponíveis:", ', '.join(map(str, catalogo.keys())))

codigo = int(input("\nDigite o código do produto que deseja consultar: "))

if codigo in catalogo:
    nome, preco = catalogo[codigo]
    print(f"\nProduto encontrado:")
    print(f"Nome: {nome}")
    print(f"Preço: R${preco:.2f}")
else:
    print("Código não encontrado no catálogo.")

