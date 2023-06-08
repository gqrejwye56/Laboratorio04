from interpreter import draw
from chessPictures import *

# Crear la base del tablero (un cuadro negro seguido de un cuadro blanco)
base = cuadrado.join(cuadrado.negative())
negativeBase = base.negative()

# Crear una fila del tablero
row = base.horizontalRepeat(4)
negativeRow = negativeBase.horizontalRepeat(4)

# Combinar las filas en pares, alternando entre una fila y su negativo
rowPair = row.up(negativeRow)

# Crear una figura compuesta por las filas repetidas verticalmente
figure = rowPair.verticalRepeat(2)

# Dibujar la figura
draw(figure)