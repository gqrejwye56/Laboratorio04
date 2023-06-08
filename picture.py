from colors import *

# Clase Picture que representa una imagen o figura
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    vertical = self.img[::-1]
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    length = len(self.img[0])
    newimg = []

    for r in self.img:
      row = ""
      x = 0
      while x < length:
        row += r[length -1 -x]
        x += 1
      newimg.append(row)

    return Picture(newimg)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    newimg = []

    for r in self.img:
      x = 0
      row = ""
      while x < len(r):
        row += self._invColor(r[x])
        x += 1
      newimg.append(row)

    return Picture(newimg)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    newimg = []
    x = 0
    while x < len(self.img):
      newimg.append(self.img[x] + p.img[x])
      x += 1

    return Picture(newimg)

  def up(self, p):
    newimg = []
    for r in self.img:
      newimg.append(r)

    for r in p.img:
      newimg.append(r)
    return Picture(newimg)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    newimg = []
    for r in p.img:
      newimg.append(r)

    for r in self.img:
      newimg.append(r)

    return Picture(newimg)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    newimg = []

    for r in self.img:
      x = 1
      row = ""
      while x <= n:
        row += r
        x += 1
      newimg.append(row)

    return Picture(newimg)

  def verticalRepeat(self, n):
    newimg = []

    x = 1
    while x <= n:
      for r in self.img:
        newimg.append(r)
      x += 1

    return Picture(newimg)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    newimg = []
    i = 0
    while (i < len(self.img[0])):
      row = ""
      j = len(self.img) - 1
      while (j >= 0):
        aux = self.img[j]
        row += aux[i]
        j -= 1
      newimg.append(row)
      i += 1
      
    return Picture(newimg)
  
  def setBackground(self, p):
    backgroundColor = p.img[0][0]
    newimg = []
    for r in self.img:
      x = 0
      row = ""
      while x < len(r): 
        if r[x] == " ":
          row += backgroundColor
        else:
          row += r[x]
        x += 1
      newimg.append(row)

    return Picture(newimg)