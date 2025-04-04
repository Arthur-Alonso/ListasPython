"""
2 - Escreva um programa que solicite ao usuário o nome de um arquivo para leitura. O
programa deve tentar abrir o arquivo e exibir seu conteúdo. Utilize tratamento de
exceções para lidar com a ausência do arquivo e outros possíveis erros.
"""

def arquivo():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

arquivo()
