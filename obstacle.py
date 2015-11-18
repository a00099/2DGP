#__author__ = 'JU'

from pico2d import *

import random

class Plane:
    image = None

    def __init__(self):
        self.state = 0
        self.x, self.y = random.randint(50,550), random.randint(500,750)
        if Plane.image == None:
            self.image = load_image('plane.png')

    def update(self):
        if self.state == 1:
            if self.y < -100:
                self.x = random.randint(50,250)
                self.y = random.randint(1000,1200)
            else:
                self.y -= 2

    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x-55,self.y-30,self.x+50,self.y+30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Helicopter:
    image = None

    def __init__(self):
        self.flag = 0
        self.state = 0
        self.x, self.y = random.randint(50,550), random.randint(500,750)
        if Plane.image == None:
            self.image = load_image('heli.png')

    def update(self):
        if self.state == 1:
            if self.y < -100:
                self.x = random.randint(50,250)
                self.y = random.randint(1000,1200)
            else:
                self.y -= 2

    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x-50,self.y-35,self.x+50,self.y+35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


