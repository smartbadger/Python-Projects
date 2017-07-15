#Title: A fish game
#Date: Feb 10, 2017
#Creators: Ariane, Connor, Corey 
#Purpose: Something to do when the internet is out to pass the time. 

#import the good stuff
import pygame
import os
import random
import time
from socket import *
from pygame.locals import *


##Function from Pygame Tutorial to load images
#------------------------------------------------------
def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

# Fish Class -what the player eats
#-------------------------------------------------------
class Fish(pygame.sprite.Sprite):

    def __init__(self, (x,y)):
        pygame.sprite.Sprite.__init__(self)
        self.speed = x
        self.sizeMult = y
        self.image = pygame.image.load("badfish.png")
        self.test = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(116*self.sizeMult), int(68*self.sizeMult)))
        screen = pygame.display.get_surface()
        randomYCoord = random.randint(100,500) 
        self.rect = self.image.get_rect(topleft = (1000,randomYCoord)) 
        
        
    def update(self, direction):
        self.rect = self.rect.move(direction)
        return self.rect

    # self-destruct    
    def die(self):
           self = None

#   Player Class - what the players uses
#----------------------------------------------------------------------
        
class Player(Fish):
    def __init__(self):
        self.size = 1.0
        self.score = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fish.png")
        self.collide = self.image.get_rect()
        self.screen = pygame.display.get_surface()
        self.rect = self.image.get_rect(topleft = (0,300))

    # player eats other fish and grows
    def grow(self):
        self.size += 0.05
        self.score += 100
        self.image = pygame.transform.scale(self.image, (int(116*self.size),int(68*self.size)))
        print "SCORE: " +str(self.score)

    # player's fish died...
    def die(self):    
            print "Player Loses"
            print "Final Score: " +str(self.score)

    #player chooses where to move (up, down)
    def move(self, background):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.update((0,-15))
                    self.screen.blit(background, self.rect, self.rect)                   
                    
                if event.key == pygame.K_DOWN:
                    self.update((0,15))
                    self.screen.blit(background, self.rect, self.rect)
                    

# Gamekeeper Class - preforms essential game functions and manages game objects
#----------------------------------------------------------------------------------
class GameKeeper():
    
    def __init__(self):
        self.status = True
        self.fishArray = []
        self.maxFish = 0
        self.player = Player()

        #  A sprite container to keep the fish managable 
        self.SpriteContainer = pygame.sprite.Group()
        self.SpriteContainer.add(self.player)


    #what the fish will look like    
    def generateProperties(self):
        speed = random.randint(1,6)*-1
        size = (random.randint(1,5)/2.5)
        return (speed, size)

    #how fish are made    
    def createFish(self):
        if self.maxFish <= 3:
            self.fishArray.append(Fish(self.generateProperties()))
            self.SpriteContainer.add(self.fishArray)
            self.maxFish+=1
        
    
    #Swimming instructions for fish        
    def controlEnemies(self, screen, background):
        for item in self.fishArray:       
            screen.blit(background, item.rect, item.rect)
            if item.update((item.speed,0))[0] < -675:
                self.removeObject(item)
            if pygame.sprite.collide_rect(self.player, item):
                self.compareSize(item)
                
    #prepares fish objects for death       
    def removeObject(self, item):
        self.SpriteContainer.remove(item)
        self.fishArray.remove(item)
        item.die()
        self.maxFish-=1

    #Enforces the laws of the food-chain
    def compareSize(self, item):
        if self.player.size < item.sizeMult:
            print "player death"
            self.status = False
        else:
            self.player.grow()
            
            self.removeObject(item)

    #how likley a fish will spawn
    def chanceToGenerate(self):   
        rand = random.randint(0,100)
        if rand == 1:
            self.createFish()

    


#Main --- no explanation needed
#-----------------------------------------------------------------------   
                    
def main():
    
    #Initialize the screen
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Fish Frenzy")

    #Initializes the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((150,150,150))

    gameWarden = GameKeeper()
    gameWarden.createFish()
    #Initialize the Fish Sprite
    
    #Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #Set clock up to cap FPS
    clock = pygame.time.Clock()    

    #Main game loop
###################################################################
    while gameWarden.status == True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        clock.tick(60)

        #do your stuff gameWarden
        gameWarden.chanceToGenerate()
        gameWarden.player.move(background)
        gameWarden.controlEnemies(screen, background)
        gameWarden.SpriteContainer.draw(screen)

        pygame.display.flip()
        
    print "GAME OVER"    
#######################################################################
main()

