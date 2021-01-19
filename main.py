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
        self.playAnimation = []
        self.healAnimation = []
        self.sadAnimation = []
        self.deathAnimation = []
        self.currentAnimation = "idle"
        self.pooCounter = 0
        self.pooCoordinates = [(600,400), (30,300), (500,200)]
        self.energy = 100
        self.food = 100
        self.happiness = 100
        self.hygiene = 100
        self.health = 100
        self.sad = 0
        self.ill = 0
        self.death = 0
        self.animationFrame = 0
        self.poo = pygame.image.load("poop.png")
        self.illness = pygame.image.load("ill.png")
        addFrames(self.idleAnimation,"idle_anim.png")
        addFrames(self.cleanAnimation, "clean_anim.png")
        addFrames(self.deathAnimation, "death_anim.png")
        addFrames(self.healAnimation, "heal_anim.png")
        addFrames(self.eatAnimation, "eat_anim.png")
        addFrames(self.sleepAnimation, "sleep_anim.png")
        addFrames(self.sadAnimation, "sad_anim.png")
        addFrames(self.playAnimation, "play_anim.png")


    # Executes current animation
    def animate(self):
        if self.currentAnimation == "idle" and self.happiness > 40:
            self.animationLoop(self.idleAnimation)
        if self.currentAnimation == "idle" and self.happiness <= 40:
            self.animationLoop(self.sadAnimation)
        if self.currentAnimation == "clean":
            self.clean()
        if self.currentAnimation == "death":
            self.animationLoop(self.deathAnimation)
        if self.currentAnimation == "heal":
            self.healing()
        if self.currentAnimation == "eat":
            self.eat()
        if self.currentAnimation == "sleep":
            self.sleep()
        if self.currentAnimation == "play":
            self.play()


    # Displays poop on the screen
    def poop(self):
        if self.pooCounter < 3:
            screen.blit(self.poo, self.pooCoordinates[self.pooCounter])
            pygame.display.update(self.pooCoordinates[self.pooCounter], (80, 80))
            self.pooCounter += 1


    # Draws healing animation
    def healing(self):
        self.frameDrawing(self.healAnimation)
        if self.animationFrame >= len(self.healAnimation):
            self.ill = 0
            self.health = 100
            self.animationFrame = 0
            self.currentAnimation = "idle"
            pygame.draw.rect(screen, (255, 255, 255), (80, 200, 120, 120))
            pygame.display.update((80, 200), (120, 120))

    # Draws clean animation
    def clean(self):
        self.frameDrawing(self.cleanAnimation)
        if self.animationFrame >= len(self.cleanAnimation):
            pygame.draw.rect(screen, (255, 255, 255), (600, 400, 80, 80))
            pygame.draw.rect(screen, (255, 255, 255), (30, 300, 80, 80))
            pygame.draw.rect(screen, (255, 255, 255), (500, 200, 80, 80))
            pygame.display.update((600, 400, 80, 80))
            pygame.display.update((30, 300, 80, 80))
            pygame.display.update((500, 200, 80, 80))
            self.pooCounter = 0
            self.hygiene = 100
            self.animationFrame = 0
            self.currentAnimation = "idle"

    # Draws eat animation
    def eat(self):
        self.frameDrawing(self.eatAnimation)
        if self.animationFrame >= len(self.eatAnimation):
            self.food = 100
            self.animationFrame = 0
            self.currentAnimation = "idle"

    # Draws sleep animation
    def sleep(self):
        self.frameDrawing(self.sleepAnimation)
        if self.animationFrame >= len(self.sleepAnimation):
            self.energy+=10
            if self.energy > 100:
                self.energy = 100
            self.animationFrame = 0
        if self.energy >= 100:
            self.currentAnimation = "idle"

    # Draws play animation
    def play(self):
        self.frameDrawing(self.playAnimation)
        if self.animationFrame >= len(self.playAnimation):
            self.happiness = 100
            self.energy -= 25
            if self.energy < 0:
                self.energy = 0
            self.animationFrame = 0
            self.currentAnimation = "idle"


    # Draws animation in a loop
    def animationLoop(self, animation):
        if self.animationFrame >= len(animation):
            self.animationFrame = 0
        self.frameDrawing(animation)

    # Draws single frame of animation
    def frameDrawing(self, animation):
        pygame.draw.rect(screen, (255, 255, 255), (200, 200, 300, 300))
        screen.blit(animation[self.animationFrame], (200, 200))
        pygame.display.update(pygame.Rect(200, 200, 300, 300))
        self.animationFrame += 1

#-------------------------------------------------------------------------------------------------
# MENU CLASS -------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi
        self.sleep = pygame.image.load("sleep.png")
        self.eat = pygame.image.load("eat.png")
        self.play = pygame.image.load("play.png")
        self.clean = pygame.image.load("clean.png")
        self.heal = pygame.image.load("heal.png")
        self.reset = pygame.image.load("reset.png")

    def displayButtons(self):
        screen.blit(self.sleep, (100,0))
        pygame.display.update((100,0), (100, 100))

        screen.blit(self.eat, (300, 0))
        pygame.display.update((300, 0), (100, 100))

        screen.blit(self.play, (500, 0))
        pygame.display.update((500, 0), (100, 100))

        screen.blit(self.clean, (100, 600))
        pygame.display.update((100, 600), (100, 100))

        screen.blit(self.heal, (300, 600))
        pygame.display.update((300, 600), (100, 100))

        screen.blit(self.reset, (500, 600))
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




#-------------------------------------------------------------------------------------------------
# MAIN -------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
def main():
    pygame.init()
    tamagotchi = Pet()
    menu = Menu(tamagotchi)
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
                x, y = event.pos

            # reset
                if ((500 <= x <= 600) and (600 <= y <= 700)):
                    pygame.draw.rect(screen, (255, 255, 255), (0, 100, 700, 500))
                    tamagotchi = Pet()
                    menu.tamagotchi = tamagotchi

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



    #HUNGER (LOWERING FOOD)
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
            screen.blit(tamagotchi.illness, (80,200))
            pygame.display.update((80,200), (120, 120))
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


    # DISPLAYING TAMAGOTCHI ANIMATIONS
        if frameCount % 20 == 0:
            print("energy:"+str(tamagotchi.energy))
            print("food:"+str(tamagotchi.food))
            print("happiness:"+str(tamagotchi.happiness))
            print("hygiene:"+str(tamagotchi.hygiene))
            print("health:"+str(tamagotchi.health))
            print("sad:"+str(tamagotchi.sad))
            print("ill:"+str(tamagotchi.ill))
            print("death:"+str(tamagotchi.death))
            tamagotchi.animate()



        frameCount += 1
        fpsClock.tick(FPS)

main()
pygame.quit()