class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f"Nome: {vingadores.nome} Ano: {vingadores.ano} Duração: {vingadores.duracao} Likes: {vingadores.likes}")

flash = Serie("the flash", 2017, 6)
flash.dar_like()
flash.dar_like()
print(f"Nome: {flash.nome} Ano: {flash.ano} Duração: {flash.temporadas} Likes: {flash.likes}")
