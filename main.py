# Szymon Romanowski projekt PJF - tamagotchi
#-------------------------------------------------------------------------------------------------
# MAIN -------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
import pygame
import random

from Menu import Menu
from Pet import Pet
from Display import Display

    # Main game logic
def main():
    pygame.init()
    screen = Display()
    tamagotchi = Pet(screen.display)
    menu = Menu(tamagotchi, screen.display)
    frameCount = 0

    screen.display.fill((255, 255, 255))
    screen.update()
    menu.displayButtons()

    running = True

    # GAME LOOP
    while running:

    # EVENTS HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

            # reset
                if ((500 <= x <= 600) and (600 <= y <= 700)):
                    pygame.draw.rect(screen.display, (255, 255, 255), (0, 100, 700, 500))
                    tamagotchi = Pet(screen.display)
                    menu.tamagotchi = tamagotchi
                    print("RESET")

                menu.handleMouse(x,y)


    # POOPING
        if frameCount % 1000 == 999:
          rand = random.randint(0, 2)
          if rand == 1:
            tamagotchi.poop()

    # LOWERING HYGIENE
        if tamagotchi.pooCounter > 0:
            if frameCount % 50 == 0:
                if tamagotchi.hygiene < 30:
                    tamagotchi.ill = 1

                if tamagotchi.hygiene <= 0:
                    tamagotchi.hygiene = 0
                else:
                    tamagotchi.hygiene -= 1 * tamagotchi.pooCounter



    # HUNGER (LOWERING FOOD)
        if frameCount % 70 == 0:
            if(tamagotchi.food > 0):
                tamagotchi.food -= 1
            else:
                tamagotchi.food = 0

            if(tamagotchi.food < 20):
                tamagotchi.health -= 1


    # BOREDOM (LOWERING HAPPINESS)
        if frameCount % 80 == 0:
            if tamagotchi.happiness > 0:
                tamagotchi.happiness -= 1
            else:
                tamagotchi.happiness = 0

    # ILLNESS
        if tamagotchi.ill == 1:
            screen.blit(tamagotchi.illness, (80, 200))
            pygame.display.update((80, 200), (120, 120))
            if frameCount % 100 == 0:
                tamagotchi.health -= 1

    # HEALTH
        if tamagotchi.health < 0:
            tamagotchi.health = 0

    # DEATH
        if tamagotchi.health <= 0:
            if tamagotchi.death == 0:
                tamagotchi.animationFrame = 0
                tamagotchi.currentAnimation = "death"
                tamagotchi.death = 1


    # PRINT TAMAGOTCHI VARIABLES
        if frameCount % 20 == 0:
            print("energy:"+str(tamagotchi.energy))
            print("food:"+str(tamagotchi.food))
            print("happiness:"+str(tamagotchi.happiness))
            print("hygiene:"+str(tamagotchi.hygiene))
            print("health:"+str(tamagotchi.health))
            print("sad:"+str(tamagotchi.sad))
            print("ill:"+str(tamagotchi.ill))
            print("death:"+str(tamagotchi.death))

    # DISPLAYING TAMAGOTCHI ANIMATIONS
        tamagotchi.animate()
        frameCount += 1
        screen.fpsClock.tick(screen.FPS)

main()
pygame.quit()