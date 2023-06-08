from interpreter import draw
from chessPictures import *

# Crear una imagen del cuadro negro
negativeSquare = cuadrado.negative()

# Crear imágenes de las piezas negras y establecer el fondo adecuado
torreNegra1 = laTorre.negative().setBackground(cuadrado)
caballoNegro1 = elCaballo.negative().setBackground(negativeSquare)
alfilNegro1 = elAlfil.negative().setBackground(cuadrado)
reynaNegra = laReina.negative().setBackground(negativeSquare)
reyNegro = elRey.negative().setBackground(cuadrado)
alfilNegro2 = elAlfil.negative().setBackground(negativeSquare)
caballoNegro2 = elCaballo.negative().setBackground(cuadrado)
torreNegra2 = laTorre.negative().setBackground(negativeSquare)

# Crear una fila de las piezas negras
row1 = torreNegra1.join(caballoNegro1).join(alfilNegro1).join(reynaNegra).join(reyNegro).join(alfilNegro2).join(caballoNegro2).join(torreNegra1)

# Crear un par de peones negros
coupleBlackPawn = elPeon.negative().setBackground(negativeSquare).join(elPeon.negative().setBackground(cuadrado))

# Crear una segunda fila de los peones negros
row2 = coupleBlackPawn.horizontalRepeat(4)

# Crear una base del tablero
base = cuadrado.join(cuadrado.negative())
negativeBase = base.negative()

# Crear una fila del tablero
row = base.horizontalRepeat(4)
negativeRow = negativeBase.horizontalRepeat(4)

# Combinar las filas de manera alternada
rowPair = row.up(negativeRow)

# Crear las filas 3 a 6 del tablero
row3_6 = rowPair.verticalRepeat(2)

# Crear la séptima fila del tablero
row7 = row2.negative()

# Crear la octava fila del tablero
row8 = row1.negative()

# Dibujar el tablero completo
draw(row1.up(row2).up(row3_6).up(row7).up(row8))