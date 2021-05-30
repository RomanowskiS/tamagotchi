#-------------------------------------------------------------------------------------------------
# PET CLASS --------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
import pygame

class Pet:
    def __init__(self, screen):
        self.screen = screen
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
        self.poo = pygame.image.load("img/poop.png")
        self.illness = pygame.image.load("img/ill.png")
        self.addFrames(self.idleAnimation,"img/idle_anim.png")
        self.addFrames(self.cleanAnimation, "img/clean_anim.png")
        self.addFrames(self.deathAnimation, "img/death_anim.png")
        self.addFrames(self.healAnimation, "img/heal_anim.png")
        self.addFrames(self.eatAnimation, "img/eat_anim.png")
        self.addFrames(self.sleepAnimation, "img/sleep_anim.png")
        self.addFrames(self.sadAnimation, "img/sad_anim.png")
        self.addFrames(self.playAnimation, "img/play_anim.png")

    # Adds single frames to animation list
    def addFrames(self, animation, path):
        spriteSheet = pygame.image.load(path)
        size = spriteSheet.get_rect().size
        frameCorner = [0, 0]
        frameSize = (300, 300)
        while frameCorner[1] < size[1]:
            singleFrame = spriteSheet.subsurface(pygame.Rect(frameCorner, frameSize))
            animation.append(singleFrame)
            frameCorner[1] += 300

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
            self.screen.blit(self.poo, self.pooCoordinates[self.pooCounter])
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
            pygame.draw.rect(self.screen, (255, 255, 255), (80, 200, 120, 120))
            pygame.display.update((80, 200), (120, 120))

    # Draws clean animation
    def clean(self):
        self.frameDrawing(self.cleanAnimation)
        if self.animationFrame >= len(self.cleanAnimation):
            pygame.draw.rect(self.screen, (255, 255, 255), (600, 400, 80, 80))
            pygame.draw.rect(self.screen, (255, 255, 255), (30, 300, 80, 80))
            pygame.draw.rect(self.screen, (255, 255, 255), (500, 200, 80, 80))
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
        pygame.draw.rect(self.screen, (255, 255, 255), (200, 200, 300, 300))
        self.screen.blit(animation[self.animationFrame], (200, 200))
        pygame.display.update(pygame.Rect(200, 200, 300, 300))
        self.animationFrame += 1
