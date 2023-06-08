from interpreter import draw
from chessPictures import *

# Crear la base del patrón (un cuadro blanco seguido de un cuadro negro)
base = cuadrado.join(cuadrado.negative())

# Crear una figura compuesta por la repetición horizontal de la base
figure = base.horizontalRepeat(4)

# Dibujar la figura
draw(figure)