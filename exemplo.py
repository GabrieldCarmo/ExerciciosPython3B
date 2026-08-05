class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar(self):
        print(f"Produto: {self.nome} | Preço: {self.preco}")

p1 = Produto("mouse", 50)
p1.mostrar()

p2 = Produto("teclado", 70)
p2.mostrar()
