"""
3 - Crie um dicionário que contenha algumas palavras em português como chave e
suas respectivas traduções para inglês como valor. Permita que o usuário digite
uma palavra em português e retorne sua tradução. Caso a palavra não esteja no
dicionário, exiba uma mensagem informando que a tradução não foi encontrada.
"""

dicionario = {
    "mesa": "table",
    "cadeira": "chair",
    "porta": "door",
    "flor": "flower",
    "peixe": "fish",
    "céu": "sky",
    "dia": "day",
    "noite": "night",
    "chave": "key",
    "bola": "ball"
}

palavra_pt = input("Digite uma palavra em português para traduzir: ").strip().lower()

if palavra_pt in dicionario:
    dicionario = dicionario[palavra_pt]
    print(f"A tradução de '{palavra_pt}' para o inglês é '{dicionario}'.")
else:
    print(f"Tradução para '{palavra_pt}' não encontrada no dicionário.")
