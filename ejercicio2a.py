from interpreter import draw
from chessPictures import *

# Crear la primera línea como la unión del caballo y su negativo
line1 = elCaballo.join(elCaballo.negative())

# Crear la segunda línea como la unión del negativo del caballo y el caballo original
line2 = elCaballo.negative().join(elCaballo)

# Combinar las dos líneas en una figura
figure = line1.up(line2)

# Dibujar la figura
draw(figure)


