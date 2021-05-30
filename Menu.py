#-------------------------------------------------------------------------------------------------
# MENU CLASS -------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
import pygame


class Menu:
    def __init__(self, tamagotchi, screen):
        self.tamagotchi = tamagotchi
        self.screen = screen
        self.sleep = pygame.image.load("img/sleep.png")
        self.eat = pygame.image.load("img/eat.png")
        self.play = pygame.image.load("img/play.png")
        self.clean = pygame.image.load("img/clean.png")
        self.heal = pygame.image.load("img/heal.png")
        self.reset = pygame.image.load("img/reset.png")

    def displayButtons(self):
        self.screen.blit(self.sleep, (100,0))
        pygame.display.update((100,0), (100, 100))

        self.screen.blit(self.eat, (300, 0))
        pygame.display.update((300, 0), (100, 100))

        self.screen.blit(self.play, (500, 0))
        pygame.display.update((500, 0), (100, 100))

        self.screen.blit(self.clean, (100, 600))
        pygame.display.update((100, 600), (100, 100))

        self.screen.blit(self.heal, (300, 600))
        pygame.display.update((300, 600), (100, 100))

        self.screen.blit(self.reset, (500, 600))
        pygame.display.update((500, 600), (100, 100))

    def handleMouse(self, x, y):
        if self.tamagotchi.death == 0:
            # sleep
            if ((100 <= x <= 200) and (0 <= y <= 100)):
              if self.tamagotchi.energy < 100:
                  self.tamagotchi.animationFrame = 0
                  self.tamagotchi.currentAnimation = "sleep"
            # eat
            elif ((300 <= x <= 400) and (0 <= y <= 100)):
               if self.tamagotchi.food < 100:
                   self.tamagotchi.animationFrame = 0
                   self.tamagotchi.currentAnimation = "eat"
            # play
            elif ((500 <= x <= 600) and (0 <= y <= 100)):
               if self.tamagotchi.energy > 0:
                   self.tamagotchi.animationFrame = 0
                   self.tamagotchi.currentAnimation = "play"
            # clean
            elif ((100 <= x <= 200) and (600 <= y <= 700)):
                if self.tamagotchi.pooCounter > 0:
                    self.tamagotchi.animationFrame = 0
                    self.tamagotchi.currentAnimation = "clean"
            # heal
            elif ((300 <= x <= 400) and (600 <= y <= 700)):
                if self.tamagotchi.ill == 1:
                    self.tamagotchi.animationFrame = 0
                    self.tamagotchi.currentAnimation = "heal"



