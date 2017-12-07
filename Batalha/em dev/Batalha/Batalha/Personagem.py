from random import randrange

class Personagem():
    # Atributos do Personagem
    nome = None
    ptsForca = None
    ptsHabilidade = None
    ptsInteligencia = None
    ptsVida = None
    ptsMana = None
    kit = None

    def __init__(self, nome="Name", ptsForca=2, ptsHabilidade=2,pstInteligencia=2):
        """
        se Mago
            For = 1
            Hab = 2
            Int = 3

        se Knight
            For = 3
            Hab = 2
            Int =  1

        se Ladino
            for = 1
            hab = 3
            int = 2
        """
        self.nome = nome
        self.ptsForca = ptsForca
        self.ptsHabilidade = ptsHabilidade
        self.ptsInteligencia = pstInteligencia

    def rolarD6(self):
        return randrange(1, 7)

    def rolarAtaque(self):
        self.dado = self.rolarD6()
        if (self.dado == 1):
            return 0
        elif(self.dado == 6):
            return 100
        else:
            return self.ptsHabilidade + 2 + self.rolarD6()

    def rolarDefesa(self):
        self.dado = self.rolarD6()
        if (self.dado == 1):
            return 0
        elif(self.dado == 6):
            return 10
        else:
            return self.ptsHabilidade + 2 + self.rolarD6()

    def testeDeMorte(self):
        pass


