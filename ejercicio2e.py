from interpreter import draw
from chessPictures import *

# Crear la base del tablero (un cuadro blanco seguido de un cuadro negro)
base = cuadrado.join(cuadrado.negative())
negativeBase = base.negative()

# Crear una figura compuesta por la repetición horizontal del negativo de la base
figure = negativeBase.horizontalRepeat(4)

# Dibujar la figura
draw(figure)