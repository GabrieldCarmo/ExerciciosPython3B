class Produto:
    def __init__(self,nome, preco):
        self.nome = nome 
        self.preco = preco
    def mostrar(self):
        print(self.nome + self.preco)

def menu():
    print("\n" + "=" * 50)
    print("MENU PRINCIPAL")
    print("=" * 50)
    print("[1] Cadastrar Livro")
    print("[2] Listar Livros")
    print("[3] Buscar Livro")
    print("[4] Sair")
    print("=" * 50)

    try:
        return int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Insira um valor válido")

def cadastro():
    print("\n")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    produto = Produto(nome, preco)
    produtos.append(produto)


produtos = []

while True:
    escolha = menu()
    if escolha == 1:
        cadastro()
