# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:27:06 2024

@author: Mrang
"""

import pygame, random, simpleGE

class Car (simpleGE.Sprite):
    def __init_(self, scene):
        super().__init__(scene)
        self.setImage("carFer.png")
        self.setSize(90,50)
        self.position = (300,400)
        self.moveSpeed = 7
class Gas(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("gasC.png")
        self.setSize(20,20)
        self.reset()
        
    def Bounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
        
    def reset(self):
      self.y = 12
      self.x = random.randint(0, self.screenWidth)
      self.dy = random.randint(3, 8)
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("natureRoad.jpg")
        self.car = Car(self)
        self.sprites = [self.car]           