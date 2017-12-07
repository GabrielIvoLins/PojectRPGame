from random import randrange

class Personagem:
    def __init__(self):
        self.nome = "Conan"
        self.ataque = 8
        self.vida = 60
        self.mana = 60

    def rolarDados(self, x, y):
        self.lado = randrange(x, y)
        return self.lado

    def fazerTestes(self,dificuldade=0):
        self.dificuldade = dificuldade
        self.rolagem = self.rolarDados(1,11)
        self.testes = self.rolagem + self.dificuldade
        return self.testes

    def recuperarVida(self,recuperar=0):
        self.recuperar = recuperar
        self.recuperar += self.vida
        return self.recuperar

    def levarDano(self,dano=0):
        self.dano = dano
        self.dano = self.vida - self.dano
        return self.dano