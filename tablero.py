import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
ventana_size = (600, 600)

# Definir los colores
BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)

# Crear la ventana
ventana = pygame.display.set_mode(ventana_size)
pygame.display.set_caption("Tablero de Ajedrez")

# Tamaño de cada casilla
casilla_size = ventana_size[0] // 8

# Ciclo principal del juego
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    
    # Dibujar el tablero
    for fila in range(8):
        for columna in range(8):
            x = columna * casilla_size
            y = fila * casilla_size

            # Dibujar casillas alternadas
            if (fila + columna) % 2 == 0:
                pygame.draw.rect(ventana , BLANCO, (x, y, casilla_size, casilla_size))
            else:
                pygame.draw.rect(ventana , GRIS, (x, y, casilla_size, casilla_size))

    # Actualizar la ventana
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
