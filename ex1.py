class Produto:
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def mostrar(self):
        print(f"\nCódigo: {self.codigo} \nProduto: {self.nome} \nQuantidade: {self.quantidade} \nPreço Unitário: {self.preco}")

print("\nExercicio de POO")

p1 = Produto(1 ,"Estojo do Léo", 2, 19.97)
p1.mostrar()

