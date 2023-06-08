from interpreter import draw
from chessPictures import *

# Llama a la función draw y pasa como argumento la composición de la imagen del
# espejo vertical del caballo (elCaballo.verticalMirror()) y la imagen rotada del
# caballo (elCaballo.rotate())
draw(elCaballo.verticalMirror().join(elCaballo.rotate()))