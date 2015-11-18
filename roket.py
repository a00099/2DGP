#__author__ = 'JU'

import random

from pico2d import *


class Rocket:
    image = None
    stop_image= None

    def __init__(self):
        self.x, self.y = 300, 90
        self.frame = 0
        self.dir = 1
        self.Xstate = 0
        self.Ystate = 0
        if Rocket.stop_image == None:
            self.stop_image = load_image('rocket_stop.png')
        if Rocket.image == None:
            self.image = load_image('rocket_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        if self.Xstate == 1:            self.x -= 2
        if self.Xstate == 2:            self.x +=2
        if self.Ystate == 1:            self.y +=2
        if self.Ystate == 2:            self.y -=2

    def draw(self):
        if self.Xstate == 0:
            self.image.clip_draw(2* 60, 0, 60, 89, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 60, 0, 60, 89, self.x, self.y)

    def get_bb(self):
        return self.x-27,self.y-44,self.x+27,self.y+45

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
