#!/usr/bin/env python
#coding: utf-8

from Personagem import *
from Player import *
from Inimigo import *

# O codigo abaixo está em teste/desenvolvimento *-*

class Batalha:
    p = Player()
    i = Inimigo()

    rollPlayer = p.rolarD6
    rollInimigo = i.rolarD6

    rollAtaP = p.rolarAtaque
    rollDefP = p.rolarDefesa

    rollAtaI = i.rolarAtaque
    rollDefI = i.rolarDefesa

    @classmethod
    def iniciativa(cls):
        if cls.rollPlayer < cls.rollInimigo:
            print("O inimigo ataca 1º")
            return cls.i

        elif cls.rollPlayer > cls.rollInimigo:
            print("O jogador ataca 1º")
            return cls.p

        elif cls.rollPlayer == cls.rollInimigo:
            print("Ambos farao o teste novamente!")
            return None

    @classmethod
    def combate(cls):

        if cls.rollAtaP() > cls.rollDefI():
            cls.i.perdeVIda(10)

        elif cls.rollAtaP() <= cls.rollDefI():
            print("Defendeu")

        elif cls.rollAtaI() > cls.rollDefP():
            cls.p.perdeVIda(10)

        elif cls.rollAtaI() <= cls.rollDefP():
            print("Defendeu")

        else:pass


    def turno(self):
        pass


luta = Batalha()

luta.combate()
print(luta.iniciativa())
print(luta.rollPlayer())
print(luta.rollAtaI())

