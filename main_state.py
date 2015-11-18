import random
import math

from pico2d import *

import game_framework
import title_state

from roket import Rocket
from obstacle import Plane,Helicopter
from background import Sky,Grass

name = "MainState"

sky = None
rocket = None
plane = None
grass = None
font = None
heli = None

def enter():
    global grass,sky,rocket,plane,planes,heli
    sky = Sky()
    rocket = Rocket()
    grass = Grass()
    plane = Plane()
    heli = Helicopter()

def exit():
    global grass,sky,rocket,plane,heli
    del(sky)
    del(rocket)
    del(grass)
    del(plane)
    del(heli)

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        if event.type == SDL_KEYDOWN:
            grass.state = 1
            sky.state =1
            plane.state = 1
            heli.state = 1
            if event.key == SDLK_a:                rocket.Xstate = 1
            if event.key == SDLK_d:                rocket.Xstate = 2
            if event.key == SDLK_w:                rocket.Ystate = 1
            if event.key == SDLK_s:                rocket.Ystate = 2
        if event.type == SDL_KEYUP:
            if event.key == SDLK_a or event.key == SDLK_d or event.key == SDLK_w or event.key == SDLK_s:
                rocket.Xstate = 0
                rocket.Ystate = 0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


def update():
    rocket.update()
    plane.update()
    if collide(plane,rocket):
        plane.remove(plane)
    if collide(heli,rocket):
        heli.remove(heli)

    sky.update()
    grass.update()
    heli.update()

def draw():
    clear_canvas()
    sky.draw()
    grass.draw()
    rocket.draw()
    plane.draw()
    heli.draw()

    plane.draw_bb()
    rocket.draw_bb()
    heli.draw_bb()

    update_canvas()






