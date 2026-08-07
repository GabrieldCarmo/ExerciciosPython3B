import os

# Classes
class Produto:
    def __init__(self,nome, preco):
        self.nome = nome 
        self.preco = preco
    def mostrar(self):
        return f"{self.nome} - R${self.preco:.2f}"

# Estrutura de dados

produtos = []

# Funções de manipulação

# Cadastro
def cadastro():
    print("\n")
    nome = input("Digite o nome do produto: ")
    if not nome.strip():
        print("[Sistema] Insira um nome válido!")
        return
    try:    
        preco = float(input("Digite o valor do produto: "))
        if preco < 0:
            return
    except:
        print("[Sistema] Insira um valor válido!")
        return
    produtos.append(Produto(nome, preco))

#Listar produtos

def listar_produtos():
    for i in range(len(produtos)):
        print(f"Produto {i}: " + produtos[i].mostrar())

# Menu

def menu():
    print("\n" + "=" * 50)
    print("MENU PRINCIPAL")
    print("=" * 50)
    print("[1] Cadastrar produto")
    print("[2] Listar produtos")
    print("[3] Comprar produto")
    print("[4] Sair")
    print("=" * 50)

    try:
        return int(input("\nEscolha uma opção: "))
    except ValueError:
        return -1

# Limpar tela

def limpar_tela():
     os.system("cls" if os.name == "nt" else "clear")

# Confirmação

def confirmacao():
    while True:
        resposta = input("\nAperte enter para prosseguir ")
        # Evita da pessoa digitar qualquer coisa e ainda prosseguir 
        if resposta == "":
            break

# Lógica

while True:
    limpar_tela()
    escolha = menu()
    if escolha == 1:
        limpar_tela()
        cadastro()
    elif escolha == 2:
        limpar_tela()
        print("\n" + "=" * 50)
        print("LISTA DE PRODUTOS")
        print("=" * 50)
        listar_produtos()
        print("=" * 50)
        confirmacao()
    elif escolha == 3:
        pass
    elif escolha == 4:
        limpar_tela()
        print("[Sistema] Encerrando...")
        break
    else:
        print("\n[Sistema] Insira uma opção válida para continuar!")