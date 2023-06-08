import pygame, sys
from pygame.locals import *
from colors import *

# Función para dibujar una línea en la ventana de visualización
def parseLine(DISPLAY, y, s):
  x = 0
  for c in s:
    pygame.draw.line(DISPLAY, color[c], (x, y), (x, y))
    x += 1

# Función principal para dibujar la imagen
def draw(picture):
  try:
    img = picture.img
  except:
    img = picture
  pygame.init()

  # Crear una ventana de visualización de tamaño 640x480
  DISPLAY=pygame.display.set_mode((640, 480))
  DISPLAY.fill(BLUE)

  n = len(img)
  # Iterar sobre las líneas de la imagen y dibujarlas en la ventana
  for i in range(0, n):
    parseLine(DISPLAY, i, img[i])

  while True:
    # Manejar eventos de pygame
    for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        #sys.exit()
    pygame.display.update()