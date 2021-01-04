# Szymon Romanowski projekt PJF - tamagotchi

import pygame
import random

FPS = 30
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode([700, 700])

# Adds single frames to animation list
def addFrames(animation, path):
    spriteSheet = pygame.image.load(path)
    size = spriteSheet.get_rect().size
    frameCorner = [0,0]
    frameSize = (300, 300)
    while frameCorner[1] < size[1]:
        singleFrame = spriteSheet.subsurface(pygame.Rect(frameCorner, frameSize))
        animation.append(singleFrame)
        frameCorner[1] += 300
#-------------------------------------------------------------------------------------------------
# PET CLASS --------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
class Pet:
    def __init__(self):
        self.idleAnimation = []
        self.sleepAnimation = []
        self.cleanAnimation = []
        self.eatAnimation = []
        self.illAnimation = []
        self.healAnimation = []
        self.currentAnimation = "idle"
        self.poo = pygame.image.load("poop.png")
        self.pooCounter = 0
        self.pooCoordinates = [(600,400), (30,300), (500,160)]
        self.energy = 100
        self.food = 100
        self.happiness = 100
        self.hygiene = 100
        self.health = 100
        self.death = 0
        self.animationFrame = 0
        addFrames(self.idleAnimation,"idle.png")

    # Executes current animation
    def animate(self):
        if self.currentAnimation == "idle":
            self.idle()


    # Displays poop on the screen
    def poop(self):
        if self.pooCounter < 3:
            screen.blit(self.poo, self.pooCoordinates[self.pooCounter])
            pygame.display.update(self.pooCoordinates[self.pooCounter], (80, 80))
            self.pooCounter += 1

    # Draws idle animation
    def idle(self):
        if self.animationFrame >= len(self.idleAnimation):
            self.animationFrame = 0

        pygame.draw.rect(screen, (255,255,255), (200, 200, 300, 300))
        screen.blit(self.idleAnimation[self.animationFrame], (200, 200))
        pygame.display.update(pygame.Rect(200, 200, 300, 300))
        self.animationFrame += 1

#-------------------------------------------------------------------------------------------------
# MENU CLASS -------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self):
        self.sleep = pygame.image.load("sleep.png")
        self.eat = pygame.image.load("eat.png")
        self.play = pygame.image.load("play.png")
        self.clean = pygame.image.load("clean.png")
        self.heal = pygame.image.load("heal.png")
        self.reset = pygame.image.load("reset.png")

    def displayButtons(self):
        screen.blit(self.sleep, (62,0))
        pygame.display.update((62,0), (150, 150))

        screen.blit(self.eat, (274, 0))
        pygame.display.update((274, 0), (150, 150))

        screen.blit(self.play, (486, 0))
        pygame.display.update((486, 0), (150, 150))

        screen.blit(self.clean, (62, 550))
        pygame.display.update((62, 550), (150, 150))

        screen.blit(self.heal, (274, 550))
        pygame.display.update((274, 550), (150, 150))

        screen.blit(self.reset, (486, 550))
        pygame.display.update((486, 550), (150, 150))

    def handleMouse(self, position):
        print(position)








#-------------------------------------------------------------------------------------------------
# MAIN -------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
def main():
    pygame.init()
    tamagotchi = Pet()
    menu = Menu()
    frameCount = 0

    screen.fill((255, 255, 255))
    pygame.display.update()
    menu.displayButtons()

    running = True

    # GAME LOOP
    while running:

    # EVENTS HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu.handleMouse(event.pos)


    # POOPING
        if frameCount % 300 == 299:
          rand = random.randint(0, 1)
          print(rand)
          if rand == 1:
            tamagotchi.poop()

    # LOWERING HYGIENE
        if tamagotchi.pooCounter > 0:
            if frameCount % 50 == 0:
                tamagotchi.hygiene -= 1 * tamagotchi.pooCounter
                print(tamagotchi.hygiene)





    # DISPLAYING TAMAGOTCHI ANIMATIONS
        if frameCount % 30 == 0:
            tamagotchi.animate()

        frameCount += 1
        fpsClock.tick(FPS)

main()
pygame.quit()