from Personagem import *

p = Personagem("Antaghus")
e = Personagem("Demonius")


"""

batalha envolve Player(s) + Inimigo(s)

batalha exige prioridade 
    ROLARINICIATIVA

Inicio da batalha
    
Batalha envolve ações
    Atacar
        Físico
        Magia
            Curar (vc ou aliado)
            Ressucitar (aliado)

    oponente 
        Esquiva
        e ou 
        Defender

    Dano
        se dano maior que HP 
            morre! game over...
        se não 
        testa a morte
        
        
    Ações Extrar
        Fugir
        Acessar Inventario (caso tenha)
            Itens de cura (hp, mp, status..., ressucitar aliado)
            Itens de dano
"""
