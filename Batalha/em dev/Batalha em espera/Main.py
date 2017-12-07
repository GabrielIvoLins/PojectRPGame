from Personagem import *
from Heroi import *
from Bandido import *

class Main():
    heroi = Heroi()
    bandido = Bandido()
    heroi.fazerTestes(10)

    rollHeroi = heroi.rolarDados(1,11)
    rollBandido = bandido.rolarDados(1,11)

    if rollHeroi < rollBandido:
        print(heroi,"Ataca antes")

    else:
        print(heroi,"Ataca depois")
