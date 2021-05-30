#-------------------------------------------------------------------------------------------------
# DISPLAY CLASS -------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
import pygame

class Display:
    def __init__(self):
        self.FPS = 3
        self.fpsClock = pygame.time.Clock()
        self.display = pygame.display.set_mode([700, 700])

    def update(self):
        pygame.display.update()