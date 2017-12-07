#!/usr/bin/env python
#coding: utf-8

desenvolvedores = """
            Gabriel Ivo Lins (Desenvolvedor)
            Kleber Galvão (Desenvolvedor Orientador)"""

"""Todos os dados são um D6,apenas para testes,
Todos valores definidos são apenas para testes,
possiveis ajustes ainda serão efetuados =D
"""

from random import randrange

class Personagem:
    def __init__(self):
        self.nome = "Conan"
        self.ataque = 8
        self.dano = 10
        self.defesa = 10
        self.vida = 50
        self.mana = 45

    def rolarD6(self):
        return randrange(1, 7)

    def rolarAtaque(self):
        return self.ataque + self.dano + self.rolarD6()

    def rolarDefesa(self):
        return self.defesa + 4 + self.rolarD6()

    # cura padrão, recupera apenas 8 de vida
    def recuperarVida(self):
        pass

    def repuperaMana(self,M=10):
        self.mana += M

    def perdeVIda(self,V=0):
        self.vida -= V
        return self.vida
